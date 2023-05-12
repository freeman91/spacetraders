from time import sleep
from pprint import pprint, pformat
from typing import List
from pydash import find

from client import Client

class ShipNav:
    pass

class ShipCargo:
    pass

class ShipCrew:
    pass

class ShipFuel:
    pass

class ShipFrame:
    pass

class ShipReactor:
    pass

class ShipEngine:
    pass

class ShipModule:
    pass

class ShipMount:
    pass

class ShipRegistration:
    pass


class Ship:
    symbol: str
    nav: ShipNav
    cargo: ShipCargo
    crew: ShipCrew
    fuel: ShipFuel
    frame: ShipFrame
    reactor: ShipReactor
    engine: ShipEngine
    modules: List[ShipModule]
    mounts:  List[ShipMount]
    registration: ShipRegistration
    

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

    def __init__(self, **kwargs):
        pprint(kwargs)
        # result = get_request(f"my/ships/{symbol}")
        # self.symbol = result.get("symbol")
        # self.nav = result.get("nav")
        # self.crew = result.get("crew")
        # self.fuel = result.get("fuel")
        # self.frame = result.get("frame")
        # self.reactor = result.get("reactor")
        # self.engine = result.get("engine")
        # self.modules = result.get("modules")
        # self.mounts = result.get("mounts")
        # self.registration = result.get("registration")
        # self.cargo = result.get("cargo")

    # def nav_wait(self):
    #     wait = 50

    #     if self.engine.get("symbol") == "ENGINE_ION_DRIVE_I":
    #         wait = 35
    #     elif self.engine.get("symbol") == "ENGINE_ION_DRIVE_II":
    #         wait = 25

    #     log_message(f". . . Wait {wait} seconds")
    #     sleep(wait)

    # def extract_wait(self):
    #     wait = 100
    #     mining_mount = find(
    #         self.mounts, lambda mount: mount["symbol"].startswith("MOUNT_MINING")
    #     ).get("symbol")

    #     if mining_mount == "MOUNT_MINING_LASER_I":
    #         wait = 70
    #     elif mining_mount == "MOUNT_MINING_LASER_II":
    #         wait = 80

    #     log_message(f"Cooldown . . . Wait {wait} seconds")
    #     sleep(wait)

    # def get_cargo(self):
    #     sleep(.5)
    #     result = get_request(f"my/ships/{self.symbol}/cargo")
    #     if result:
    #         self.cargo = result

    # def get_nav(self):
    #     result = get_request(f"my/ships/{self.symbol}/nav")
    #     self.nav = result
    #     return result

    # def cooldown(self):
    #     result = get_request(f"my/ships/{self.symbol}/cooldown")
    #     if result != {}:
    #         remaining = result.get("remainingSeconds")
    #         return f"{remaining} seconds remaining"

    #     return "ready for extraction"

    # def navigate(self, waypoint: str):
    #     result = post_request(
    #         f"my/ships/{self.symbol}/navigate", {"waypointSymbol": waypoint}
    #     )
    #     self.nav = result["nav"]
    #     self.fuel = result["fuel"]
    #     log_message(
    #         self.symbol
    #         + f" in transit to {self.nav.get('route').get('destination').get('symbol')}"
    #     )

    # def dock(self):
    #     result = post_request(f"my/ships/{self.symbol}/dock")

    #     nav = result.get("nav")
    #     if nav:
    #         self.nav = nav
    #         log_message(self.symbol + f" docked at {self.nav.get('waypointSymbol')}")
        
    #     else:
    #         sleep(5)
    #         self.dock()

    # def orbit(self):
    #     result = post_request(f"my/ships/{self.symbol}/orbit")
    #     self.nav = result["nav"]
    #     log_message(self.symbol + f" orbiting {self.nav.get('waypointSymbol')}")

    # def survey(self):
    #     result = post_request(f"my/ships/{self.symbol}/survey", log=True)
    #     pprint(result)
    #     return result

    # def refuel(self, agent):
    #     result = post_request(f"my/ships/{self.symbol}/refuel")
    #     self.fuel = result["fuel"]
    #     agent.credits = result["agent"]["credits"]

    #     log_message(self.symbol + " refueled")

    # def extract(self):
    #     result = post_request(f"my/ships/{self.symbol}/extract")
    #     self.cargo = result.get("cargo")
    #     extraction = result.get('extraction', {})
    #     log_message(self.symbol + f" extracted: {extraction.get('yield')}")

    # def sell(self, agent, _symbol: str, units: int):
    #     result = post_request(
    #         f"my/ships/{self.symbol}/sell",
    #         {"symbol": _symbol, "units": int(units)},
    #     )

    #     agent.credits = result["agent"]["credits"]
    #     self.cargo = result["cargo"]

    #     transaction = result["transaction"]
    #     response = {
    #         "symbol": transaction.get("tradeSymbol"),
    #         "units": transaction.get("units"),
    #         "total": transaction.get("totalPrice"),
    #         "pricePerUnit": transaction.get("pricePerUnit"),
    #     }

    #     log_message(self.symbol + f" sold: {pformat(response)}")
    #     sleep(.5)
    #     return result["transaction"]
