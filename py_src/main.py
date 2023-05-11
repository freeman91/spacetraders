from time import sleep
from pprint import pprint
from pydash import find, filter_

from agent import Agent
from waypoint import Waypoint
from __util__ import log_message


PLANET = "X1-DF55-20250Z"
ASTEROID_FIELD = "X1-DF55-17335A"


def sell_trade_goods(_ship, _contract):
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


def extract_sell_til_enough(_ship, _contract):
    while True:
        _ship.get_cargo()
        units = _ship.cargo.get("units")
        capacity = _ship.cargo.get("capacity")
        log_message(f"Cargo: {units} / {capacity}")

        if units < capacity:
            _ship.extract()
            log_message("Cooldown . . . Wait 70s")
            sleep(70)

        else:
            _ship.dock()
            sell_trade_goods(_ship, _contract)

            _ship.orbit()

        contract_good_in_inventory = find(
            _ship.cargo.get("inventory"),
            lambda good: good.get("symbol")
            == _contract.terms.get("deliver")[0].get("tradeSymbol"),
        )
        if contract_good_in_inventory and contract_good_in_inventory.get("units") > 20:
            break


def main():
    while True:
        ship.get_nav()
        ship.get_cargo()

        # 1: Orbitting ASTEROID FIELD
        if ship.nav.get("status") == "DOCKED":
            ship.orbit()

        elif ship.nav.get("status") == "IN_TRANSIT":
            log_message(" . . . Wait 25s")
            sleep(25)

        if ship.nav.get("waypointSymbol") != ASTEROID_FIELD:
            ship.navigate(ASTEROID_FIELD)
            log_message(" . . . Wait 25s")
            sleep(25)
            ship.get_nav()

        # 2: Extract and sell until have enough Aluminum
        extract_sell_til_enough(ship, contract)

        # 4: Navigate to planet
        ship.navigate(PLANET)
        log_message(" . . . Wait 25s")
        sleep(25)
        ship.dock()

        # 5: Navigate to planet and deliver trade goods in contract
        contract.deliver(ship)

        # 6: Refuel
        ship.refuel(agent)
        ship.orbit()


def find_system_trait(idx: int, trait: str):
    system = agent.systems()[idx]
    print(system.get('symbol'))
    print()

    for waypoint in system['waypoints']:
        wp = Waypoint(waypoint.get('symbol'))
        print(wp)
        # for trait in wp.traits:
        #         if trait.get('symbol') == trait:
        #                  print(wp.symbol)
        #                  print()

def test():
    for idx in range(10):
        find_system_trait(idx, "SHIPYARD")

if __name__ == "__main__":
    agent = Agent()
    ship = agent.get_ship(0)
    contract = agent.get_contract(0)
    system = agent.get_system()

    