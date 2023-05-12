from datetime import datetime
from pprint import pformat, pprint
from typing import List

from pydash import find

from ship import Ship


class PaymentMap:
    on_accepted: str
    on_fulfilled: str

    def __init__(self, **kwargs) -> None:
        self.on_accepted = kwargs.get("onAccepted")
        self.on_fulfilled = kwargs.get("onFulfilled")

    def __repr__(self) -> str:
        return pformat(
            {
                "on_accepted": self.on_accepted,
                "on_fulfilled": self.on_fulfilled,
            }
        )


class DeliverMap:
    destination_symbol: str
    trade_symbol: str
    units_fulfilled: int
    units_required: int

    def __init__(self, **kwargs) -> None:
        self.destination_symbol = kwargs.get("destinationSymbol")
        self.trade_symbol = kwargs.get("tradeSymbol")
        self.units_fulfilled = kwargs.get("unitsFulfilled")
        self.units_required = kwargs.get("unitsRequired")

    def __repr__(self) -> str:
        return pformat(
            {
                "destination_symbol": self.destination_symbol,
                "trade_symbol": self.trade_symbol,
                "units_fulfilled": self.units_fulfilled,
                "units_required": self.units_required,
            }
        )


class Terms:
    deadline: str
    deliver: List[DeliverMap]
    payment: dict

    def __init__(self, **kwargs) -> None:
        self.deadline = kwargs.get("deadline")
        self.deliver = [DeliverMap(**item) for item in kwargs.get("deliver")]
        self.payment = PaymentMap(**kwargs.get("payment"))

    def __repr__(self) -> str:
        return pformat(
            {
                "deadline": self.deadline,
                "deliver": self.deliver,
                "payment": self.payment,
            }
        )


class Contract:
    id_: str
    type_: str
    accepted: bool
    expiration: str
    faction: str
    fulfilled: bool
    terms: Terms

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

    def __init__(self, **kwargs) -> None:
        self.id_ = kwargs.get("id")
        self.type_ = kwargs.get("type")
        self.accepted = kwargs.get("accepted")
        self.expiration = kwargs.get("expiration")
        self.faction = kwargs.get("factionSymbol")
        self.fulfilled = kwargs.get("fulfilled")
        self.terms = Terms(**kwargs.get("terms"))

    def log(self, message: str) -> None:
        print(f"[{datetime.now().isoformat()[:19]}] :: {self.id_} :: {message}")

    def fulfill(self, client):
        result = client.my.contracts.fulfill(self.id_)
        pprint(result)
        return result

    def deliver(self, client, ship: Ship):
        trade_symbol = self.terms.deliver[0].trade_symbol
        stored_trade_good = find(
            ship.cargo.inventory,
            lambda good: good.symbol == trade_symbol,
        )

        result = client.my.contracts.deliver(
            ship.symbol, self.id_, trade_symbol, stored_trade_good.units
        )

        ship.cargo = result.get("cargo")
        self.terms = Terms(**result.get("contract").get("terms"))
        self.log(str(stored_trade_good.units) + " " + trade_symbol + " delivered")
        self.log(
            "Contract units fulfilled: " + str(self.terms.deliver[0].units_fulfilled)
        )

        return result
