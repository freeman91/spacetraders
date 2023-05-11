import inquirer
from pydash import map_, filter_

from agent import Agent
from contract import Contract
from ship import Ship
from system import System
from waypoint import Waypoint


def contract(agent: Agent = None) -> Contract:
    """
    Select a contract.

    :param agent: Agent to use.
    :return: Contract instance
    """

    agent = agent or Agent()

    contract_ids = map_(agent.contracts(), lambda contract: contract.get("id"))
    contract_id = inquirer.prompt(
        [
            inquirer.List(
                "contract",
                message="Select a contract",
                choices=contract_ids,
            ),
        ]
    ).get("contract")

    return Contract(contract_id)


def ship(agent: Agent = None) -> Ship:
    """
    Select a ship.

    :param agent: Agent to use.
    :return: Ship instance
    """

    agent = agent or Agent()

    ship_names = map_(agent.get_ships(), lambda ship: ship.get("symbol"))
    ship_name = inquirer.prompt(
        [
            inquirer.List(
                "ship",
                message="Select a ship",
                choices=ship_names,
            ),
        ]
    ).get("ship")

    return Ship(ship_name)


def system(agent: Agent = None) -> System:
    """
    Select a system.

    :param agent: Agent to use.
    :return: System instance
    """

    agent = agent or Agent()

    systems = map_(
        agent.systems(),
        lambda system: f"{system.get('symbol')}: {system.get('type')}",
    )
    system_name = inquirer.prompt(
        [
            inquirer.List(
                "system",
                message="Select a system",
                choices=systems,
            ),
        ]
    ).get("system")

    return System(system_name.split(":")[0])


def waypoint(agent: Agent = None, _type: str = None) -> Waypoint:
    """
    Select a waypoint.

    :param agent: Agent to use.
    :return: Waypoint instance
    """

    agent = agent or Agent()

    _system = system(agent)

    waypoint_symbols = map_(
        _system.waypoints,
        lambda waypoint: f"{waypoint.get('symbol')}: {waypoint.get('type')}",
    )

    if _type:
        waypoint_symbols = filter_(
            waypoint_symbols,
            lambda waypoint: _type in waypoint,
        )

    waypoint_symbol = inquirer.prompt(
        [
            inquirer.List(
                "waypoint",
                message="Select a waypoint",
                choices=waypoint_symbols,
            ),
        ]
    ).get("waypoint")

    return Waypoint(waypoint_symbol.split(":")[0])
