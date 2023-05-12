# pylint: disable=C0103

from datetime import datetime
from time import sleep
from pprint import pprint, pformat
from typing import List

from pydash import filter_


class ShipNavRouteWaypoint:
    symbol: str
    system_symbol: str
    type: str
    x: int
    y: int

    def __init__(self, **kwargs) -> None:
        self.symbol = kwargs.get("symbol")
        self.system_symbol = kwargs.get("system_symbol")
        self.type = kwargs.get("type")
        self.x = kwargs.get("x")
        self.y = kwargs.get("y")

    def __repr__(self) -> str:
        return pformat(
            {
                "symbol": self.symbol,
                "system_symbol": self.system_symbol,
                "type": self.type,
                "x": self.x,
                "y": self.y,
            }
        )


class ShipNavRoute:
    arrival: str
    departure: ShipNavRouteWaypoint
    departure_time: str
    destination: ShipNavRouteWaypoint

    def __init__(self, **kwargs) -> None:
        self.arrival = kwargs.get("arrival")
        self.departure = ShipNavRouteWaypoint(**kwargs.get("departure"))
        self.departure_time = kwargs.get("departureTime")
        self.destination = ShipNavRouteWaypoint(**kwargs.get("destination"))

    def __repr__(self) -> str:
        return pformat(
            {
                "arrival": self.arrival,
                "departure": self.departure,
                "departure_time": self.departure_time,
                "destination": self.destination,
            }
        )


class ShipNav:
    flight_mode: str
    route: ShipNavRoute
    status: str
    system_symbol: str
    waypoint_symbol: str

    def __init__(self, **kwargs) -> None:
        self.flight_mode = kwargs.get("flightMode")
        self.route = ShipNavRoute(**kwargs.get("route"))
        self.status = kwargs.get("status")
        self.system_symbol = kwargs.get("systemSymbol")
        self.waypoint_symbol = kwargs.get("waypointSymbol")

    def __repr__(self) -> str:
        return pformat(
            {
                "flight_mode": self.flight_mode,
                "route": self.route,
                "status": self.status,
                "system_symbol": self.system_symbol,
                "waypoint_symbol": self.waypoint_symbol,
            }
        )


class ShipCargoInventoryItem:
    symbol: str
    name: str
    description: str
    units: int

    def __init__(self, **kwargs) -> None:
        self.symbol = kwargs.get("symbol")
        self.name = kwargs.get("name")
        self.description = kwargs.get("description")
        self.units = kwargs.get("units")

    def __repr__(self) -> str:
        return pformat(
            {
                "symbol": self.symbol,
                "name": self.name,
                "description": self.description,
                "units": self.units,
            }
        )


class ShipCargo:
    capacity: int
    units: int
    inventory: List[ShipCargoInventoryItem]

    def __init__(self, **kwargs) -> None:
        self.capacity = kwargs.get("capacity")
        self.units = kwargs.get("units")
        self.inventory = [
            ShipCargoInventoryItem(**item) for item in kwargs.get("inventory")
        ]

    def __repr__(self) -> str:
        return pformat(
            {
                "capacity": self.capacity,
                "units": self.units,
                "inventory": self.inventory,
            }
        )


class ShipCrew:
    capacity: int
    current: int
    morale: int
    required: int
    rotation: str
    wages: int

    def __init__(self, **kwargs) -> None:
        self.capacity = kwargs.get("capacity")
        self.current = kwargs.get("current")
        self.morale = kwargs.get("morale")
        self.morale = kwargs.get("morale")
        self.required = kwargs.get("required")
        self.rotation = kwargs.get("rotation")
        self.wages = kwargs.get("wages")

    def __repr__(self) -> str:
        return pformat(
            {
                "capacity": self.capacity,
                "current": self.current,
                "morale": self.morale,
                "required": self.required,
                "rotation": self.rotation,
                "wages": self.wages,
            }
        )


class ShipFuel:
    capacity: int
    consumed: dict
    current: int

    def __init__(self, **kwargs) -> None:
        self.capacity = kwargs.get("capacity")
        self.consumed = kwargs.get("consumed")
        self.current = kwargs.get("current")

    def __repr__(self) -> str:
        return pformat(
            {
                "capacity": self.capacity,
                "consumed": self.consumed,
                "current": self.current,
            }
        )


class ShipFrame:
    symbol: str
    name: str
    condition: int
    description: str
    fuel_capacity: int
    module_slots: int
    mounting_points: int
    requirements: dict

    def __init__(self, **kwargs) -> None:
        self.symbol = kwargs.get("symbol")
        self.name = kwargs.get("name")
        self.condition = kwargs.get("condition")
        self.description = kwargs.get("description")
        self.fuel_capacity = kwargs.get("fuelCapacity")
        self.module_slots = kwargs.get("moduleSlots")
        self.mounting_points = kwargs.get("mountingPoints")
        self.requirements = kwargs.get("requirements")

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
            }
        )


class ShipReactor:
    symbol: str
    name: str
    condition: int
    description: str
    power_output: int
    requirements: dict

    def __init__(self, **kwargs) -> None:
        self.symbol = kwargs.get("symbol")
        self.name = kwargs.get("name")
        self.condition = kwargs.get("condition")
        self.description = kwargs.get("description")
        self.power_output = kwargs.get("powerOutput")
        self.requirements = kwargs.get("requirements")

    def __repr__(self) -> str:
        return pformat(
            {
                "symbol": self.symbol,
                "name": self.name,
                "condition": self.condition,
                "description": self.description,
                "power_output": self.power_output,
                "requirements": self.requirements,
            }
        )


class ShipEngine:
    symbol: str
    name: str
    condition: int
    description: str
    speed: int
    requirements: dict

    def __init__(self, **kwargs) -> None:
        self.symbol = kwargs.get("symbol")
        self.name = kwargs.get("name")
        self.condition = kwargs.get("condition")
        self.description = kwargs.get("description")
        self.speed = kwargs.get("speed")
        self.requirements = kwargs.get("requirements")

    def __repr__(self) -> str:
        return pformat(
            {
                "symbol": self.symbol,
                "name": self.name,
                "condition": self.condition,
                "description": self.description,
                "speed": self.speed,
                "requirements": self.requirements,
            }
        )


class ShipModule:
    name: str
    symbol: str
    capacity: int
    description: str
    requirements: dict

    def __init__(self, **kwargs) -> None:
        self.name = kwargs.get("name")
        self.symbol = kwargs.get("symbol")
        self.capacity = kwargs.get("capacity")
        self.description = kwargs.get("description")
        self.requirements = kwargs.get("requirements")

    def __repr__(self) -> str:
        return pformat(
            {
                "name": self.name,
                "symbol": self.symbol,
                "capacity": self.capacity,
                "description": self.description,
                "requirements": self.requirements,
            }
        )


class ShipMount:
    name: str
    symbol: str
    description: str
    requirements: dict
    strength: int

    def __init__(self, **kwargs) -> None:
        self.name = kwargs.get("name")
        self.symbol = kwargs.get("symbol")
        self.description = kwargs.get("description")
        self.requirements = kwargs.get("requirements")
        self.strength = kwargs.get("strength")

    def __repr__(self) -> str:
        return pformat(
            {
                "name": self.name,
                "symbol": self.symbol,
                "description": self.description,
                "requirements": self.requirements,
                "strength": self.strength,
            }
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
            }
        )


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
    mounts: List[ShipMount]
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
        self.symbol = kwargs.get("symbol")
        self.nav = ShipNav(**kwargs.get("nav"))
        self.cargo = ShipCargo(**kwargs.get("cargo"))
        self.crew = ShipCrew(**kwargs.get("crew"))
        self.fuel = ShipFuel(**kwargs.get("fuel"))
        self.frame = ShipFrame(**kwargs.get("frame"))
        self.reactor = ShipReactor(**kwargs.get("reactor"))
        self.engine = ShipEngine(**kwargs.get("engine"))
        self.modules = [ShipModule(**module) for module in kwargs.get("modules", [])]
        self.mounts = [ShipMount(**mount) for mount in kwargs.get("mounts", [])]
        self.registration = ShipRegistration(**kwargs.get("registration"))

    def log(self, message: str) -> None:
        print(f"[{datetime.now().isoformat()[:19]}] :: {self.symbol} :: {message}")

    def get_nav(self, client):
        nav = client.my.ships.nav(self.symbol)
        self.nav = nav
        return nav

    def get_cargo(self, client):
        cargo = client.my.ships.cargo(self.symbol)
        if cargo:
            self.cargo = cargo
            sleep(0.5)

        return cargo

    def dock(self, client):
        nav = client.my.ships.dock(self.symbol)
        if nav:
            self.log(f"docked at {nav.waypoint_symbol}")
            return nav

        sleep(5)
        return self.dock(client)

    def orbit(self, client):
        nav = client.my.ships.orbit(self.symbol)
        if nav:
            self.log(f"orbiting {nav.waypoint_symbol}")
            return nav

        sleep(5)
        return self.orbit(client)

    def navigate(self, client, waypoint_symbol: str):
        result = client.my.ships.navigate(self.symbol, waypoint_symbol)

        self.nav = ShipNav(**result.get("nav"))
        self.fuel = ShipFuel(**result.get("fuel"))
        self.log(f"in transit to {self.nav.route.destination.symbol}")

        # TODO: subtract now from arrival to get seconds

        wait = 50

        if self.engine.symbol == "ENGINE_ION_DRIVE_I":
            wait = 35
        elif self.engine.symbol == "ENGINE_ION_DRIVE_II":
            wait = 25

        self.log(f". . . Waiting {wait} seconds")
        sleep(wait)

        return self.nav

    def extract(self, client):
        result = client.my.ships.extract(self.symbol)

        cooldown = result.get("cooldown")
        extraction = result.get("extraction")

        self.cargo = ShipCargo(**result.get("cargo"))
        self.log(f"extracted: {extraction.get('yield')}")

        wait = cooldown.get("remainingSeconds")
        self.log(f"Cooldown . . . Wait {wait} seconds")
        sleep(wait)

    def cooldown(self, client):
        result = client.my.ships.cooldown(self.symbol)
        if result != {}:
            remaining = result.get("remainingSeconds")
            return f"{remaining} seconds remaining"

        return "ready for extraction"

    def survey(self, client):
        survey = client.my.ships.survey(self.symbol)
        pprint(survey)
        return survey

    def refuel(self, client, agent):
        result = client.my.ships.refuel(self.symbol)
        self.fuel = ShipFuel(**result.get("fuel"))
        agent.credits = result.get("agent").get("credits")

        self.log("refueled")

    def sell(self, client, agent, contract):
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
            result = client.my.ships.sell(self.symbol, good.symbol, good.units)
            transaction = result["transaction"]
            response = {
                "symbol": transaction.get("tradeSymbol"),
                "units": transaction.get("units"),
                "total": transaction.get("totalPrice"),
                "pricePerUnit": transaction.get("pricePerUnit"),
            }

            self.log(f"sold: {pformat(response)}")

        agent.credits = result.get("agent", {}).get("credits")
        self.cargo = ShipCargo(**result.get("cargo"))

        sleep(0.5)
        return result["transaction"]
