from pprint import pprint, pformat
from __util__ import get_request, post_request


class Ship:
    symbol = ""
    nav = {}
    crew = {}
    fuel = {}
    frame = {}
    reactor = {}
    engine = {}
    modules = []
    mounts = []
    registration = {}
    cargo = {}

    def __repr__(self) -> str:
        return pformat(
            {
                "symbol": self.symbol,
                "nav": self.nav,
                "crew": self.crew,
                "fuel": self.fuel,
                "frame": self.frame,
                "reactor": self.reactor,
                "engine": self.engine,
                "modules": self.modules,
                "mounts": self.mounts,
                "registration": self.registration,
                "cargo": self.cargo,
            }
        )

    def __init__(self, symbol: str):
        result = get_request(f"my/ships/{symbol}")
        self.symbol = result.get("symbol")
        self.nav = result.get("nav")
        self.crew = result.get("crew")
        self.fuel = result.get("fuel")
        self.frame = result.get("frame")
        self.reactor = result.get("reactor")
        self.engine = result.get("engine")
        self.modules = result.get("modules")
        self.mounts = result.get("mounts")
        self.registration = result.get("registration")
        self.cargo = result.get("cargo")

    def get_cargo(self):
        result = get_request(f"my/ships/{self.symbol}/cargo")
        self.cargo = result

    def get_nav(self):
        result = get_request(f"my/ships/{self.symbol}/nav")
        self.nav = result

    def cooldown(self):
        try:
            remaining = get_request(f"my/ships/{self.symbol}/cooldown")[
                "remainingSeconds"
            ]
            return f"{remaining} seconds remaining"

        except Exception:
            return "ready for extraction"

    def navigate(self, waypoint: str):
        result = post_request(
            f"my/ships/{self.symbol}/navigate", {"waypointSymbol": waypoint}
        )
        self.nav = result["nav"]
        self.fuel = result["fuel"]
        print(f"in transit to {self.nav.get('route').get('destination').get('symbol')}")

    def dock(self):
        result = post_request(f"my/ships/{self.symbol}/dock")
        self.nav = result["nav"]
        print(f"docked at {self.nav.get('waypointSymbol')}")

    def orbit(self):
        result = post_request(f"my/ships/{self.symbol}/orbit")
        self.nav = result["nav"]
        print(f"orbiting {self.nav.get('waypointSymbol')}")

    def survey(self):
        result = post_request(f"my/ships/{self.symbol}/survey")
        pprint(result)
        return result

    def refuel(self, agent):
        result = post_request(f"my/ships/{self.symbol}/refuel")
        self.fuel = result["fuel"]
        agent.credits = result["agent"]["credits"]
        print("refueled")

    def extract(self):
        result = post_request(f"my/ships/{self.symbol}/extract")
        self.cargo = result.get("cargo")
        print(f"Extracted: {result['extraction']['yield']}")

    def sell(self, agent, _symbol: str, units: int):
        result = post_request(
            f"my/ships/{self.symbol}/sell",
            {"symbol": _symbol, "units": int(units)},
        )

        agent.credits = result["agent"]["credits"]
        self.cargo = result["cargo"]

        transaction = result["transaction"]
        response = {
            "symbol": transaction.get("tradeSymbol"),
            "units": transaction.get("units"),
            "total": transaction.get("totalPrice"),
            "pricePerUnit": transaction.get("pricePerUnit"),
        }
        print("Sell: ", pformat(response))
        return result["transaction"]
