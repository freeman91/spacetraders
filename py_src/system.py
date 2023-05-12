# pylint: disable=C0103

import math
from pprint import pformat
from typing import List


class SystemWaypoint:
    def __repr__(self) -> str:
        return pformat(
            {
                "symbol": self.symbol,
                "type_": self.type_,
                "x": self.x,
                "y": self.y,
            },
            indent=4,
        )

    def __init__(self, **kwargs):
        self.symbol: str = kwargs.get("symbol")
        self.type_: str = kwargs.get("type")
        self.x: int = kwargs.get("x")
        self.y: int = kwargs.get("y")


class System:
    def __init__(self, **kwargs):
        self.symbol: str = kwargs.get("symbol")
        self.type_: str = kwargs.get("type")
        self.factions: List[str] = kwargs.get("factions")
        self.sector_symbol: str = kwargs.get("sectorSymbol")
        self.waypoints: List[SystemWaypoint] = [
            SystemWaypoint(**waypoint) for waypoint in kwargs.get("waypoints", [])
        ]
        self.x: int = kwargs.get("x")
        self.y: int = kwargs.get("ymbol")

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

    def distance(self, destination):
        return math.sqrt((destination.x - self.x) ** 2 + (destination.y - self.x) ** 2)
