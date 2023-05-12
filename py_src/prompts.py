from typing import List

import inquirer
from pydash import filter_, find

from client import Client
from contract import Contract
from ship import Ship
from system import System
from waypoint import Waypoint


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


def contract(client: Client, fulfilled: bool = False) -> Contract:
    contracts = filter_(
        client.my.contracts.all(), lambda contract: contract.fulfilled is fulfilled
    )

    contracts = [
        {"name": f"{contract.faction} [{contract.id_}]", "value": contract}
        for contract in contracts
    ]

    return resource(contracts, "Contract")


def ship(client: Client) -> Ship:
    ships = [
        {"name": f"{ship.symbol}", "value": ship} for ship in client.my.ships.all()
    ]
    return resource(ships, "Ship")


def system(client: Client) -> System:
    systems = [
        {"name": f"{system.symbol} :: {system.type_}", "value": system}
        for system in client.systems.all()
    ]
    return resource(systems, "System")


def waypoint(client: Client, type_: str) -> Waypoint:
    waypoints = filter_(
        system(client).waypoints, lambda waypoint: waypoint.type_ == type_
    )

    waypoints = [
        {"name": f"{waypoint.symbol} :: {waypoint.type_}", "value": waypoint}
        for waypoint in waypoints
    ]
    return resource(waypoints, "System")
