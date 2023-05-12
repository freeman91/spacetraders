from pprint import pformat


class Agent:
    account_id: str
    credits: int
    headquarters: str
    symbol: str

    def __repr__(self) -> str:
        return pformat(
            {
                "account_id": self.account_id,
                "credits": self.credits,
                "headquarters": self.headquarters,
                "symbol": self.symbol,
            }
        )

    def __init__(self, **kwargs) -> None:
        self.account_id = kwargs.get("accountId")
        self.symbol = kwargs.get("symbol")
        self.credits = kwargs.get("credits")
        self.headquarters = kwargs.get("headquarters")
