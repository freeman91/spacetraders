from pprint import pformat, pprint

from client import Client

class Agent:
    account_id: str
    credits: int
    client: Client
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

    def __init__(self, client: Client, **kwargs) -> None:
        print(f"{client = }")
        pprint(kwargs)
        # self.account_id = account_id
        # self.symbol = symbol
        # self.credits = _credits
        # self.headquarters = headquarters
