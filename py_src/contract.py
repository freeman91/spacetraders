from pprint import pformat, pprint
from pydash import find
from __util__ import get_request, post_request, log_message


class Contract:
    id_ = ""
    _type = ""
    accepted = None
    expiration = ""
    faction = ""
    fulfilled = ""
    terms = {}

    def __repr__(self) -> str:
        return pformat(
            {
                "id": self.id_,
                "type": self._type,
                "accepted": self.accepted,
                "expiration": self.expiration,
                "faction": self.faction,
                "fulfilled": self.fulfilled,
                "terms": self.terms,
            }
        )

    def __init__(self, id_: str):
        result = get_request(f"my/contracts/{id_}")
        self.id_ = result.get("id")
        self._type = result.get("type")
        self.accepted = result.get("accepted")
        self.expiration = result.get("expiration")
        self.faction = result.get("factionSymbol")
        self.fulfilled = result.get("fulfilled")
        self.terms = result.get("terms")

    def accept(self):
        return post_request(f"my/contracts/{self.id_}/accept")

    def deliver(self, ship):
        trade_symbol = self.terms.get("deliver")[0].get("tradeSymbol")
        trade_good = find(
            ship.cargo.get("inventory"),
            lambda good: good.get("symbol") == trade_symbol,
        )

        result = post_request(
            f"my/contracts/{self.id_}/deliver",
            {
                "shipSymbol": ship.symbol,
                "tradeSymbol": trade_symbol,
                "units": trade_good.get("units"),
            },
        )


        ship.cargo = result.get('cargo')
        log_message(pformat(result.get('agent')))

        return result
