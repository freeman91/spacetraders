from pprint import pformat, pprint

from __util__ import get_request, get_system


class Waypoint:
    symbol = ""
    system_symbol = ""
    _type = ""
    faction = {}
    orbitals = []
    traits = []
    x_coord = 0
    y_coord = 0

    def __repr__(self) -> str:
        return pformat(
            {
                "symbol": self.symbol,
                "sector_symbol": self.system_symbol,
                "_type": self._type,
                "faction": self.faction,
                "orbitals": self.orbitals,
                "traits": self.traits,
                "x": self.x_coord,
                "y": self.y_coord,
            }
        )

    def __init__(self, symbol: str):
        _system = get_system(symbol)
        result = get_request(f"systems/{_system}/waypoints/{symbol}")
        self.symbol = result.get("symbol")
        self.system_symbol = result.get("systemSymbol")
        self._type = result.get("type")
        self.faction = result.get("faction")
        self.orbitals = result.get("orbitals")
        self.traits = result.get("traits")
        self.x_coord = result.get("x")
        self.y_coord = result.get("y")

    def get_market(self):
        _system = get_system(self.symbol)
        result = get_request(f"systems/{_system}/waypoints/{self.symbol}/market")
        pprint(result)
        return result

    def get_shipyard(self):
        _system = get_system(self.symbol)
        result = get_request(f"systems/{_system}/waypoints/{self.symbol}/shipyard")
        pprint(result)
        return result
