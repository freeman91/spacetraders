# pylint: disable=C0103

import math
from pprint import pformat
from typing import List


class Waypoint:
    def __repr__(self) -> str:
        return pformat(
            {
                "symbol": self.symbol,
                "sector_symbol": self.system_symbol,
                "type_": self.type_,
                "faction": self.faction,
                "orbitals": self.orbitals,
                "traits": self.traits,
                "x": self.x,
                "y": self.y,
            }
        )

    def __init__(self, **kwargs):
        self.client_systems_waypoints = kwargs.get("client")
        self.symbol: str = kwargs.get("symbol")
        self.system_symbol: str = kwargs.get("systemSymbol")
        self.type_: str = kwargs.get("type")
        self.faction: str = kwargs.get("faction")
        self.orbitals: List = kwargs.get("orbitals")
        self.traits: List = kwargs.get("traits")
        self.x: int = kwargs.get("x")
        self.y: int = kwargs.get("y")

    def market(self):
        return self.client_systems_waypoints.market(self.system_symbol, self.symbol)

    def shipyard(self):
        return self.client_systems_waypoints.shipyard(self.system_symbol, self.symbol)

    def distance(self, destination):
        return math.sqrt((destination.x - self.x) ** 2 + (destination.y - self.x) ** 2)
