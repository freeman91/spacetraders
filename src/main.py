import json
from datetime import datetime
from pprint import pprint
from time import sleep

from pydash import find

import prompts
from client import Client, register
from contract import Contract
from ship import Ship
from system import System
from waypoint import Waypoint


def log_message(message: str):
    print(f"[{datetime.now().isoformat()[:19]}] :: {message}")


def extract_and_sell(ship: Ship, contract: Contract):
    while True:
        log_message(
            f"{ship.symbol} :: Cargo: {ship.cargo.units} / {ship.cargo.capacity}"
        )

        if ship.cargo.units <= ship.cargo.capacity * 0.9:
            ship.extract()

        else:
            ship.dock()
            ship.sell(contract)
            ship.orbit()

        contract_good = find(
            ship.cargo.inventory,
            lambda good: good.symbol == contract.terms.deliver[0].trade_symbol,
        )
        if contract_good and contract_good.units >= ship.cargo.capacity / 2:
            break


def extract_loop(ship: Ship, contract: Contract, waypoint: Waypoint):
    while True:
        # 1: Orbiting _waypooint
        if ship.nav.status == "DOCKED":
            ship.orbit()

        elif ship.nav.status == "IN_TRANSIT":
            sleep(30)

        if ship.nav.waypoint_symbol != waypoint.symbol:
            ship.navigate(waypoint.symbol)

        # 2: Extract and sell until have enough _contract trade
        extract_and_sell(ship, contract)

        # 4: Navigate to planet
        ship.navigate(contract.terms.deliver[0].destination_symbol)
        ship.dock()

        # 5: Deliver trade goods in contract
        contract.deliver(ship)

        # 6: Refuel
        ship.refuel()
        ship.orbit()


def setup_extraction_loop():
    log_message("Setup Extraction Loop...")

    ship = prompts.ship()
    contract = prompts.contract()
    waypoint = prompts.waypoint(ship.nav.system_symbol, "ASTEROID_FIELD")

    extract_loop(ship, contract, waypoint)


def _agent():
    return Client().my.agent()


def _contract():
    result = prompts.contract()
    deliver = result.terms.deliver[0]
    print(
        f"Contract {deliver.units_fulfilled / deliver.units_required * 100:.2f}% fulfilled"
    )
    return result


def _orbital_station():
    return Client().systems.waypoints.get("X1-YP35", "X1-YP35-94217X")


def _write_all_systems_to_file():
    all_systems = Client().systems.full_list()
    with open("systems.json", "w", encoding="utf-8") as file:
        json.dump(all_systems, file, indent=4)


def _system() -> System:
    return Client().systems.get("X1-YP35")


def print_waypoints(system_symbol: str):
    system = Client().systems.get(system_symbol)
    pprint(system.waypoints)


def test():
    # system = Client().systems.get('X1-JZ7')
    pass


if __name__ == "__main__":
    pass
