
import math
from pprint import pformat, pprint
from typing import List

from client import Client
from waypoint import Waypoint


class System(Client):
    symbol: str
    type_: str
    factions: List
    sector_symbol: str
    waypoints: List
    x_coord: int
    y_coord: int

    def __repr__(self) -> str:
        return pformat(
            {
                "symbol": self.symbol,
                "type_": self.type_,
                "factions": self.factions,
                "sector_symbol": self.sector_symbol,
                "waypoints": self.waypoints,
                "x_coord": self.x_coord,
                "y_coord": self.y_coord,
            }
        )

    def __init__(self, **kwargs):
        pprint(kwargs)
    #     result = get_request(f"systems/{symbol}")
    #     self.symbol = result.get("symbol")
    #     self.type_ = result.get("type")
    #     self.factions = result.get("factions")
    #     self.sector_symbol = result.get("sectorSymbol")
    #     self.waypoints = result.get("waypoints")
    #     self.x_coord = result.get("x")
    #     self.y_coord = result.get("y")

    # def get_waypoint_idx(self, idx):
    #     return Waypoint(self.waypoints[idx].get("symbol"))

    # def distance(self, destination):
    #     return math.sqrt((destination.x_coord - self.x_coord)**2 + (destination.y_coord - self.x_coord)**2)