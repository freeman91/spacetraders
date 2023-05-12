from datetime import datetime
from time import sleep

from pydash import find

import prompts
from agent import Agent
from client import Client
from contract import Contract
from ship import Ship
from waypoint import Waypoint


def extract_and_sell(
    client: Client, agent: Agent, ship: Ship, contract: Contract, threshold: int = 30
):
    while True:
        log_message(
            f"{ship.symbol} :: Cargo: {ship.cargo.units} / {ship.cargo.capacity}"
        )

        if ship.cargo.units < ship.cargo.capacity:
            ship.extract(client)

        else:
            ship.dock(client)
            ship.sell(client, agent, contract)
            ship.orbit(client)

        contract_good = find(
            ship.cargo.inventory,
            lambda good: good.symbol == contract.terms.deliver[0].trade_symbol,
        )
        if contract_good and contract_good.units > threshold:
            break


def extract_loop(
    client: Client, agent: Agent, ship: Ship, contract: Contract, waypoint: Waypoint
):
    while True:
        # 1: Orbiting _waypooint
        if ship.nav.status == "DOCKED":
            ship.orbit(client)

        elif ship.nav.status == "IN_TRANSIT":
            sleep(30)

        if ship.nav.waypoint_symbol != waypoint.symbol:
            ship.navigate(client, waypoint.symbol)

        # 2: Extract and sell until have enough _contract trade
        extract_and_sell(client, agent, ship, contract)

        # 4: Navigate to planet
        ship.navigate(client, contract.terms.deliver[0].destination_symbol)
        ship.dock(client)

        # 5: Deliver trade goods in contract
        contract.deliver(client, ship)

        # 6: Refuel
        ship.refuel(client, agent)
        ship.orbit(client)


def log_message(message: str):
    print(f"[{datetime.now().isoformat()[:19]}] :: {message}")


def setup_extraction_loop():
    client = Client()
    agent = client.my.agent()
    log_message("Setup Extraction Loop...")

    ship = prompts.ship(client)
    contract = prompts.contract(client)
    waypoint = prompts.waypoint(client, "ASTEROID_FIELD")

    extract_loop(client, agent, ship, contract, waypoint)


if __name__ == "__main__":
    pass
