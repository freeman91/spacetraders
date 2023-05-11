from pydash import find, filter_

import prompts
from agent import Agent
from contract import Contract
from ship import Ship
from waypoint import Waypoint
from __util__ import log_message


agent = Agent()


def sell_trade_goods(_ship: Ship, _contract: Contract):
    # sell all trade goods not aluminum or antimatter
    sellable_goods = filter_(
        _ship.cargo.get("inventory"),
        lambda trade_good: trade_good.get("symbol")
        not in (
            "ANTIMATTER",
            _contract.terms.get("deliver")[0].get("tradeSymbol"),
        ),
    )
    for good in sellable_goods:
        _ship.sell(agent, good.get("symbol"), good.get("units"))


def extract_sell_til_enough(_ship: Ship, _contract: Contract):
    while True:
        _ship.get_cargo()
        units = _ship.cargo.get("units")
        capacity = _ship.cargo.get("capacity")
        log_message(f"Cargo: {units} / {capacity}")

        if units < capacity:
            _ship.extract()
            _ship.extract_wait()

        else:
            _ship.dock()
            sell_trade_goods(_ship, _contract)
            _ship.orbit()

        contract_good_in_inventory = find(
            _ship.cargo.get("inventory"),
            lambda good: good.get("symbol")
            == _contract.terms.get("deliver")[0].get("tradeSymbol"),
        )
        if contract_good_in_inventory and contract_good_in_inventory.get("units") > 30:
            break


def extract_loop(_ship: Ship, _contract: Contract, _waypoint: Waypoint):
    _ship.get_nav()

    while True:
        # 1: Orbitting _waypooint
        if _ship.nav.get("status") == "DOCKED":
            _ship.orbit()

        elif _ship.nav.get("status") == "IN_TRANSIT":
            _ship.nav_wait()

        if _ship.nav.get("waypointSymbol") != _waypoint.symbol:
            _ship.navigate(_waypoint.symbol)
            _ship.nav_wait()
            _ship.get_nav()

        # 2: Extract and sell until have enough _contract trade
        extract_sell_til_enough(_ship, _contract)

        # 4: Navigate to planet
        _ship.navigate(_contract.terms.get("deliver")[0].get("destinationSymbol"))
        _ship.nav_wait()
        _ship.dock()

        # 5: Deliver trade goods in contract
        _contract.deliver(_ship)

        # 6: Refuel
        _ship.refuel(agent)
        _ship.orbit()


def setup_extraction_loop():
    log_message("Setup Extraction Loop...")
    ship = prompts.ship(agent)
    contract = prompts.contract(agent)
    waypoint = prompts.waypoint(agent, "ASTEROID_FIELD")

    extract_loop(ship, contract, waypoint)


if __name__ == "__main__":
    pass
