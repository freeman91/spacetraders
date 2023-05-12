# pylint: disable=C0103

import math
from pprint import pformat, pprint
from typing import List


class Waypoint:
    symbol: str
    system_symbol: str
    type_: str
    faction: str
    orbitals: List
    traits: List
    x: int
    y: int

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
        self.symbol = kwargs.get("symbolx")
        self.system_symbol = kwargs.get("system_symbol")
        self.type_ = kwargs.get("type")
        self.faction = kwargs.get("faction")
        self.orbitals = kwargs.get("orbitals")
        self.traits = kwargs.get("traits")
        self.x = kwargs.get("x")
        self.y = kwargs.get("y")

    def market(self, client):
        result = client.systems.waypoints.market(self.system_symbol, self.symbol)
        pprint(result)
        return result

    def shipyard(self, client):
        result = client.systems.waypoints.shipyard(self.system_symbol, self.symbol)
        pprint(result)
        return result

    def distance(self, destination):
        return math.sqrt((destination.x - self.x) ** 2 + (destination.y - self.x) ** 2)
