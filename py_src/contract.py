from pprint import pformat
from typing import List

from pydash import find


class Terms:
    pass

class Contract:
    id_: str
    type_: str
    accepted: bool
    expiration: str
    faction: str
    fulfilled: bool
    terms: List[Terms]

    def __repr__(self) -> str:
        return pformat(
            {
                "id": self.id_,
                "type_": self.type_,
                "accepted": self.accepted,
                "expiration": self.expiration,
                "faction": self.faction,
                "fulfilled": self.fulfilled,
                "terms": self.terms,
            }
        )

    def __init__(self, **kwargs):
        print(f"{kwargs = }")
        
        # self.id_ = result.get("id")
        # self._type = result.get("type")
        # self.accepted = result.get("accepted")
        # self.expiration = result.get("expiration")
        # self.faction = result.get("factionSymbol")
        # self.fulfilled = result.get("fulfilled")
        # self.terms = result.get("terms")

    # def accept(self):
    #     return post_request(f"my/contracts/{self.id_}/accept")
    
    # def accept(self):
    #     return post_request(f"my/contracts/{self.id_}/fulfill")

    # def deliver(self, ship):
    #     trade_symbol = self.terms.get("deliver")[0].get("tradeSymbol")
    #     trade_good = find(
    #         ship.cargo.get("inventory"),
    #         lambda good: good.get("symbol") == trade_symbol,
    #     )
    #     units = trade_good.get("units")

    #     result = post_request(
    #         f"my/contracts/{self.id_}/deliver",
    #         {
    #             "shipSymbol": ship.symbol,
    #             "tradeSymbol": trade_symbol,
    #             "units": units,
    #         },
    #     )

    #     ship.cargo = result.get("cargo")
    #     self.terms = result.get("contract").get("terms")
    #     log_message(str(units) + " " + trade_symbol + " delivered")
    #     log_message("Fulfilled: " + str(self.terms.get("deliver")[0].get("unitsFulfilled", 0)))

    #     return result
