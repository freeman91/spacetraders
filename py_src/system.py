from pprint import pformat

from __util__ import get_request
from waypoint import Waypoint


class System:
    symbol = ""
    _type = ""
    factions = []
    sector_symbol = ""
    waypoints = []
    x_coord = 0
    y_coord = 0

    def __repr__(self) -> str:
        return pformat(
            {
                "symbol": self.symbol,
                "_type": self._type,
                "factions": self.factions,
                "sector_symbol": self.sector_symbol,
                "waypoints": self.waypoints,
                "x": self.x_coord,
                "y": self.y_coord,
            }
        )

    def __init__(self, symbol: str):
        result = get_request(f"systems/{symbol}")
        self.symbol = result.get("symbol")
        self._type = result.get("type")
        self.factions = result.get("factions")
        self.sector_symbol = result.get("sectorSymbol")
        self.waypoints = result.get("waypoints")
        self.x_coord = result.get("x")
        self.y_coord = result.get("y")

    def get_waypoint_idx(self, idx):
        return Waypoint(self.waypoints[idx].get("symbol"))
