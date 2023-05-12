
import math
from pprint import pformat, pprint
from typing import List

from client import Client

class Waypoint(Client):
    symbol: str
    system_symbol: str
    _type: str
    faction: str
    orbitals: List
    traits: List
    x_coord: int
    y_coord: int

    def __repr__(self) -> str:
        return pformat(
            {
                "symbol": self.symbol,
                "sector_symbol": self.system_symbol,
                "_type": self._type,
                "faction": self.faction,
                "orbitals": self.orbitals,
                "traits": self.traits,
                "x_coord": self.x_coord,
                "y_coord": self.y_coord,
            }
        )

    def __init__(self, **kwargs):
        pprint(kwargs)
        # _system = get_system(symbol)
        # result = get_request(f"systems/{_system}/waypoints/{symbol}")
        # self.symbol = result.get("symbol")
        # self.system_symbol = result.get("systemSymbol")
        # self._type = result.get("type")
        # self.faction = result.get("faction")
        # self.orbitals = result.get("orbitals")
        # self.traits = result.get("traits")
        # self.x_coord = result.get("x")
        # self.y_coord = result.get("y")

    # def get_market(self):
    #     _system = get_system(self.symbol)
    #     result = get_request(f"systems/{_system}/waypoints/{self.symbol}/market")
    #     pprint(result)
    #     return result

    # def get_shipyard(self):
    #     _system = get_system(self.symbol)
    #     result = get_request(f"systems/{_system}/waypoints/{self.symbol}/shipyard")
    #     pprint(result)
    #     return result

    def distance(self, destination):
        return math.sqrt((destination.x_coord - self.x_coord)**2 + (destination.y_coord - self.x_coord)**2)