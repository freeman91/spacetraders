from pprint import pformat, pprint
from __util__ import get_request, get_system, post_request
from contract import Contract
from system import System
from ship import Ship


class Agent:
    account_id = ""
    credits = 0
    headquarters = ""
    symbol = ""
    faction = "COSMIC"

    def __repr__(self) -> str:
        return pformat(
            {
                "account_id": self.account_id,
                "credits": self.credits,
                "headquarters": self.headquarters,
                "symbol": self.symbol,
            }
        )

    def __init__(self) -> None:
        result = get_request("my/agent")

        self.account_id = result.get("accountId")
        self.symbol = result.get("symbol")
        self.credits = result.get("credits")
        self.headquarters = result.get("headquarters")

    def contracts(self):
        return get_request("my/contracts")

    def get_contract(self, idx):
        contracts = self.contracts()
        return Contract(contracts[idx]["id"])

    def get_system(self):
        return System(get_system(self.headquarters))

    def systems(self):
        return get_request("systems")

    def get_ships(self):
        return get_request("my/ships")

    def get_ship(self, idx):
        ships = self.get_ships()
        return Ship(ships[idx]["symbol"])

    def purchase_ship(self, ship_type: str, waypoint: str):
        result = post_request("my/ships", {"shipType": ship_type, "waypointSymbol": waypoint})
        pprint(result)
        return result