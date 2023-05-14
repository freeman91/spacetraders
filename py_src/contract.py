from datetime import datetime
from pprint import pformat, pprint
from typing import List

from pydash import find

from ship import Ship, ShipCargo


class PaymentMap:
    def __init__(self, **kwargs) -> None:
        self.on_accepted: str = kwargs.get("onAccepted")
        self.on_fulfilled: str = kwargs.get("onFulfilled")

    def __repr__(self) -> str:
        return pformat(
            {
                "on_accepted": self.on_accepted,
                "on_fulfilled": self.on_fulfilled,
            },
            indent=8,
        )


class DeliverMap:
    def __init__(self, **kwargs) -> None:
        self.destination_symbol: str = kwargs.get("destinationSymbol")
        self.trade_symbol: str = kwargs.get("tradeSymbol")
        self.units_fulfilled: int = kwargs.get("unitsFulfilled")
        self.units_required: int = kwargs.get("unitsRequired")

    def __repr__(self) -> str:
        return pformat(
            {
                "destination_symbol": self.destination_symbol,
                "trade_symbol": self.trade_symbol,
                "units_fulfilled": self.units_fulfilled,
                "units_required": self.units_required,
            },
            indent=8,
        )


class Terms:
    def __init__(self, **kwargs) -> None:
        self.deadline: str = kwargs.get("deadline")
        self.deliver: List[DeliverMap] = [
            DeliverMap(**item) for item in kwargs.get("deliver")
        ]
        self.payment: PaymentMap = PaymentMap(**kwargs.get("payment"))

    def __repr__(self) -> str:
        return pformat(
            {
                "deadline": self.deadline,
                "deliver": self.deliver,
                "payment": self.payment,
            },
            indent=4,
        )


class Contract:
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
        self.client_my_contracts: str = kwargs.get("client")
        self.id_: str = kwargs.get("id")
        self.type_: str = kwargs.get("type")
        self.accepted: bool = kwargs.get("accepted")
        self.expiration: str = kwargs.get("expiration")
        self.faction: str = kwargs.get("factionSymbol")
        self.fulfilled: bool = kwargs.get("fulfilled")
        self.terms: Terms = Terms(**kwargs.get("terms"))

    def log(self, message: str) -> None:
        print(f"[{datetime.now().isoformat()[:19]}] :: {self.id_} :: {message}")

    def fulfill(self):
        result = self.client_my_contracts.fulfill(self.id_)
        pprint(result)
        return result

    def accept(self):
        result = self.client_my_contracts.accept(self.id_)
        pprint(result)
        return result

    def deliver(self, ship: Ship):
        trade_symbol = self.terms.deliver[0].trade_symbol
        stored_trade_good = find(
            ship.cargo.inventory,
            lambda good: good.symbol == trade_symbol,
        )

        result = self.client_my_contracts.deliver(
            ship.symbol, self.id_, trade_symbol, stored_trade_good.units
        )

        ship.cargo = ShipCargo(**result.get("cargo"))
        self.terms = Terms(**result.get("contract").get("terms"))
        self.log(str(stored_trade_good.units) + " " + trade_symbol + " delivered")
        self.log(
            "Contract units fulfilled: " + str(self.terms.deliver[0].units_fulfilled)
        )

        return result
