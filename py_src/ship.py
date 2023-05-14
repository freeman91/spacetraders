# pylint: disable=C0103

from datetime import datetime
from time import sleep
from pprint import pprint, pformat
from typing import List

from pydash import filter_


class ShipNavRouteWaypoint:
    def __init__(self, **kwargs) -> None:
        self.symbol: str = kwargs.get("symbol")
        self.system_symbol: str = kwargs.get("systemSymbol")
        self.type_: str = kwargs.get("type")
        self.x: int = kwargs.get("x")
        self.y: int = kwargs.get("y")

    def __repr__(self) -> str:
        return pformat(
            {
                "symbol": self.symbol,
                "system_symbol": self.system_symbol,
                "type_": self.type_,
                "x": self.x,
                "y": self.y,
            },
            indent=8,
        )


class ShipNavRoute:
    def __init__(self, **kwargs) -> None:
        self.arrival: str = kwargs.get("arrival")
        self.departure: ShipNavRouteWaypoint = ShipNavRouteWaypoint(
            **kwargs.get("departure")
        )
        self.departure_time: str = kwargs.get("departureTime")
        self.destination: ShipNavRouteWaypoint = ShipNavRouteWaypoint(
            **kwargs.get("destination")
        )

    def __repr__(self) -> str:
        return pformat(
            {
                "arrival": self.arrival,
                "departure": self.departure,
                "departure_time": self.departure_time,
                "destination": self.destination,
            },
            indent=8,
        )


class ShipNav:
    def __init__(self, **kwargs) -> None:
        self.flight_mode: str = kwargs.get("flightMode")
        self.route: ShipNavRoute = ShipNavRoute(**kwargs.get("route"))
        self.status: str = kwargs.get("status")
        self.system_symbol: str = kwargs.get("systemSymbol")
        self.waypoint_symbol: str = kwargs.get("waypointSymbol")

    def __repr__(self) -> str:
        return pformat(
            {
                "flight_mode": self.flight_mode,
                "route": self.route,
                "status": self.status,
                "system_symbol": self.system_symbol,
                "waypoint_symbol": self.waypoint_symbol,
            },
            indent=4,
        )


class ShipCargoInventoryItem:
    def __init__(self, **kwargs) -> None:
        self.symbol: str = kwargs.get("symbol")
        self.name: str = kwargs.get("name")
        self.description: str = kwargs.get("description")
        self.units: int = kwargs.get("units")

    def __repr__(self) -> str:
        return pformat(
            {
                "symbol": self.symbol,
                "name": self.name,
                "description": self.description,
                "units": self.units,
            },
            indent=8,
        )


class ShipCargo:
    def __init__(self, **kwargs) -> None:
        self.capacity: int = kwargs.get("capacity")
        self.units: int = kwargs.get("units")
        self.inventory: List[ShipCargoInventoryItem] = [
            ShipCargoInventoryItem(**item) for item in kwargs.get("inventory")
        ]

    def __repr__(self) -> str:
        return pformat(
            {
                "capacity": self.capacity,
                "units": self.units,
                "inventory": self.inventory,
            },
            indent=4,
        )


class ShipCrew:
    def __init__(self, **kwargs) -> None:
        self.capacity: int = kwargs.get("capacity")
        self.current: int = kwargs.get("current")
        self.morale: int = kwargs.get("morale")
        self.required: int = kwargs.get("required")
        self.rotation: str = kwargs.get("rotation")
        self.wages: int = kwargs.get("wages")

    def __repr__(self) -> str:
        return pformat(
            {
                "capacity": self.capacity,
                "current": self.current,
                "morale": self.morale,
                "required": self.required,
                "rotation": self.rotation,
                "wages": self.wages,
            },
            indent=4,
        )


class ShipFuel:
    def __init__(self, **kwargs) -> None:
        self.capacity: int = kwargs.get("capacity")
        self.consumed: dict = kwargs.get("consumed")
        self.current: int = kwargs.get("current")

    def __repr__(self) -> str:
        return pformat(
            {
                "capacity": self.capacity,
                "consumed": self.consumed,
                "current": self.current,
            },
            indent=4,
        )


class ShipFrame:
    def __init__(self, **kwargs) -> None:
        self.symbol: str = kwargs.get("symbol")
        self.name: str = kwargs.get("name")
        self.condition: int = kwargs.get("condition")
        self.description: str = kwargs.get("description")
        self.fuel_capacity: int = kwargs.get("fuelCapacity")
        self.module_slots: int = kwargs.get("moduleSlots")
        self.mounting_points: int = kwargs.get("mountingPoints")
        self.requirements: dict = kwargs.get("requirements")

    def __repr__(self) -> str:
        return pformat(
            {
                "symbol": self.symbol,
                "name": self.name,
                "condition": self.condition,
                "description": self.description,
                "fuel_capacity": self.fuel_capacity,
                "module_slots": self.module_slots,
                "mounting_points": self.mounting_points,
                "requirements": self.requirements,
            },
            indent=4,
        )


class ShipReactor:
    def __init__(self, **kwargs) -> None:
        self.symbol: str = kwargs.get("symbol")
        self.name: str = kwargs.get("name")
        self.condition: int = kwargs.get("condition")
        self.description: str = kwargs.get("description")
        self.power_output: int = kwargs.get("powerOutput")
        self.requirements: dict = kwargs.get("requirements")

    def __repr__(self) -> str:
        return pformat(
            {
                "symbol": self.symbol,
                "name": self.name,
                "condition": self.condition,
                "description": self.description,
                "power_output": self.power_output,
                "requirements": self.requirements,
            },
            indent=4,
        )


class ShipEngine:
    def __init__(self, **kwargs) -> None:
        self.symbol: str = kwargs.get("symbol")
        self.name: str = kwargs.get("name")
        self.condition: int = kwargs.get("condition")
        self.description: str = kwargs.get("description")
        self.speed: int = kwargs.get("speed")
        self.requirements: dict = kwargs.get("requirements")

    def __repr__(self) -> str:
        return pformat(
            {
                "symbol": self.symbol,
                "name": self.name,
                "condition": self.condition,
                "description": self.description,
                "speed": self.speed,
                "requirements": self.requirements,
            },
            indent=4,
        )


class ShipModule:
    def __init__(self, **kwargs) -> None:
        self.name: str = kwargs.get("name")
        self.symbol: str = kwargs.get("symbol")
        self.capacity: int = kwargs.get("capacity")
        self.description: str = kwargs.get("description")
        self.requirements: dict = kwargs.get("requirements")

    def __repr__(self) -> str:
        return pformat(
            {
                "name": self.name,
                "symbol": self.symbol,
                "capacity": self.capacity,
                "description": self.description,
                "requirements": self.requirements,
            },
            indent=8,
        )


class ShipMount:
    def __init__(self, **kwargs) -> None:
        self.name: str = kwargs.get("name")
        self.symbol: str = kwargs.get("symbol")
        self.description: str = kwargs.get("description")
        self.requirements: dict = kwargs.get("requirements")
        self.strength: int = kwargs.get("strength")

    def __repr__(self) -> str:
        return pformat(
            {
                "name": self.name,
                "symbol": self.symbol,
                "description": self.description,
                "requirements": self.requirements,
                "strength": self.strength,
            },
            indent=8,
        )


class ShipRegistration:
    faction_symbol: str
    name: str
    role: str

    def __init__(self, **kwargs) -> None:
        self.faction_symbol = kwargs.get("factionSymbol")
        self.name = kwargs.get("name")
        self.role = kwargs.get("role")

    def __repr__(self) -> str:
        return pformat(
            {
                "faction_symbol": self.faction_symbol,
                "name": self.name,
                "role": self.role,
            },
            indent=4,
        )


class Ship:
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
        self.client_my_ships = kwargs.get("client")
        self.symbol: str = kwargs.get("symbol")
        self.nav: ShipNav = ShipNav(**kwargs.get("nav"))
        self.cargo: ShipCargo = ShipCargo(**kwargs.get("cargo"))
        self.crew: ShipCrew = ShipCrew(**kwargs.get("crew"))
        self.fuel: ShipFuel = ShipFuel(**kwargs.get("fuel"))
        self.frame: ShipFrame = ShipFrame(**kwargs.get("frame"))
        self.reactor: ShipReactor = ShipReactor(**kwargs.get("reactor"))
        self.engine: ShipEngine = ShipEngine(**kwargs.get("engine"))
        self.modules: List[ShipModule] = [
            ShipModule(**module) for module in kwargs.get("modules", [])
        ]
        self.mounts: List[ShipMount] = [
            ShipMount(**mount) for mount in kwargs.get("mounts", [])
        ]
        self.registration: ShipRegistration = ShipRegistration(
            **kwargs.get("registration")
        )

    def log(self, message: str) -> None:
        print(f"[{datetime.now().isoformat()[:19]}] :: {self.symbol} :: {message}")

    def get_nav(self):
        nav = self.client_my_ships.nav(self.symbol)
        self.nav = nav
        return nav

    def get_cargo(self):
        cargo = self.client_my_ships.cargo(self.symbol)
        if cargo:
            self.cargo = cargo
            sleep(0.5)

        return cargo

    def dock(self):
        nav = self.client_my_ships.dock(self.symbol)
        if nav:
            self.log(f"docked at {nav.waypoint_symbol}")
            return nav

        sleep(5)
        return self.dock()

    def orbit(self):
        nav = self.client_my_ships.orbit(self.symbol)
        if nav:
            self.log(f"orbiting {nav.waypoint_symbol}")
            return nav

        sleep(5)
        return self.orbit()

    def navigate(self, waypoint_symbol: str):
        result = self.client_my_ships.navigate(
            self.symbol,
            waypoint_symbol,
        )

        self.nav = ShipNav(**result.get("nav"))
        self.fuel = ShipFuel(**result.get("fuel"))
        self.log(f"in transit to {self.nav.route.destination.symbol}")

        arrival = datetime.strptime(self.nav.route.arrival, "%Y-%m-%dT%H:%M:%S.%fZ")
        now = datetime.utcnow()

        wait = (arrival - now).seconds
        self.log(f". . . Waiting {wait} seconds")
        sleep(wait)
        return self.nav

    def extract(self):
        result = self.client_my_ships.extract(self.symbol)

        cooldown = result.get("cooldown")
        extraction = result.get("extraction")

        self.cargo = ShipCargo(**result.get("cargo"))
        self.log(f"extracted: {extraction.get('yield')}")

        wait = cooldown.get("remainingSeconds")
        self.log(f"Cooldown . . . Wait {wait} seconds")
        sleep(wait)

    def cooldown(self):
        result = self.client_my_ships.cooldown(self.symbol)
        if result != {}:
            remaining = result.get("remainingSeconds")
            return f"{remaining} seconds remaining"

        return "ready for extraction"

    def survey(self):
        survey = self.client_my_ships.survey(self.symbol)
        pprint(survey)
        return survey

    def refuel(self):
        result = self.client_my_ships.refuel(self.symbol)
        self.fuel = ShipFuel(**result.get("fuel"))
        self.log("refueled")

    def sell(self, contract):
        sellable_goods = filter_(
            self.cargo.inventory,
            lambda trade_good: trade_good.symbol
            not in (
                "ANTIMATTER",
                contract.terms.deliver[0].trade_symbol,
            ),
        )

        result = None
        for good in sellable_goods:
            result = self.client_my_ships.sell(self.symbol, good.symbol, good.units)
            transaction = result["transaction"]
            response = {
                "symbol": transaction.get("tradeSymbol"),
                "units": transaction.get("units"),
                "total": transaction.get("totalPrice"),
                "pricePerUnit": transaction.get("pricePerUnit"),
            }

            self.log(f"sold: {pformat(response)}")

        self.cargo = ShipCargo(**result.get("cargo"))

        sleep(0.5)
        return result["transaction"]

    def purchase(self, ship_type: str, waypoint):
        result = self.client_my_ships.purchase(ship_type, waypoint.symbol)
        pprint(result.get("transaction"))
