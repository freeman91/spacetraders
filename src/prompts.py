from typing import List

import inquirer
from pydash import filter_, find

from contract import Contract
from ship import Ship
from system import System
from waypoint import Waypoint
from client import Client


def resource(resources: List, resource_type: str):
    if len(resources) == 1:
        return resources[0].get("value")

    _resource = inquirer.prompt(
        [
            inquirer.List(
                "RESOURCE",
                message=f"Select {resource_type}",
                choices=[resource["name"] for resource in resources],
                carousel=True,
            )
        ]
    ).get("RESOURCE")

    if not _resource:
        raise ValueError(f"You must select a {resource_type}")

    return find(resources, lambda resource: resource["name"] == _resource).get("value")


def contract(fulfilled: bool = None) -> Contract:
    contracts = Client().my.contracts.all()

    if isinstance(fulfilled, bool):
        contracts = filter_(contracts, lambda contract: contract.fulfilled == fulfilled)

    if not contracts:
        return None

    contracts = [
        {"name": f"{contract.faction} [{contract.id_}]", "value": contract}
        for contract in contracts
    ]

    return resource(contracts, "Contract")


def ship() -> Ship:
    ships = [
        {
            "name": f"{ship.symbol} :: {ship.registration.role} :: \
{ship.frame.symbol.replace('FRAME_', '')}",
            "value": ship,
        }
        for ship in Client().my.ships.all()
    ]
    return resource(ships, "Ship")


def system() -> System:
    systems = [
        {
            "name": f"{system.symbol} :: {system.type_} :: ({system.x}, {system.y})",
            "value": system,
        }
        for system in Client().systems.all()
    ]
    return resource(systems, "System")


def waypoint(system_symbol: str = None, type_: str = None) -> Waypoint:
    system_ = Client().systems.get(system_symbol)
    waypoints = system_.waypoints
    if type_:
        waypoints = filter_(system_.waypoints, lambda waypoint: waypoint.type_ == type_)

    waypoints = [
        {"name": f"{waypoint.symbol} :: {waypoint.type_}", "value": waypoint}
        for waypoint in waypoints
    ]
    waypoint_ = resource(waypoints, "System")
    return Client().systems.waypoints.get(system_.symbol, waypoint_.symbol)


def ship_type(ship_types: List[str]) -> str:
    return resource(ship_types, "Ship Type")
