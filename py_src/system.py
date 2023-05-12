# pylint: disable=C0103

import math
from pprint import pformat
from typing import List


class SystemWaypoint:
    symbol: str
    type_: str
    x: int
    y: int

    def __repr__(self) -> str:
        return pformat(
            {
                "symbol": self.symbol,
                "type_": self.type_,
                "x": self.x,
                "y": self.y,
            }
        )

    def __init__(self, **kwargs):
        self.symbol = kwargs.get("symbol")
        self.type_ = kwargs.get("type")
        self.x = kwargs.get("x")
        self.y = kwargs.get("y")


class System:
    symbol: str
    type_: str
    factions: List
    sector_symbol: str
    waypoints: List
    x: int
    y: int

    def __repr__(self) -> str:
        return pformat(
            {
                "symbol": self.symbol,
                "type_": self.type_,
                "factions": self.factions,
                "sector_symbol": self.sector_symbol,
                "waypoints": self.waypoints,
                "x": self.x,
                "y": self.y,
            }
        )

    def __init__(self, **kwargs):
        self.symbol = kwargs.get("symbol")
        self.type_ = kwargs.get("type")
        self.factions = kwargs.get("factions")
        self.sector_symbol = kwargs.get("sectorSymbol")
        self.waypoints = [
            SystemWaypoint(**waypoint) for waypoint in kwargs.get("waypoints", [])
        ]
        self.x = kwargs.get("x")
        self.y = kwargs.get("ymbol")

    def distance(self, destination):
        return math.sqrt((destination.x - self.x) ** 2 + (destination.y - self.x) ** 2)
