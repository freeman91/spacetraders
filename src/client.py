# pylint: disable=C0103

import os
from pprint import pprint

from dotenv import load_dotenv
import requests

from agent import Agent
from contract import Contract
from ship import Ship, ShipCargo, ShipNav
from system import System
from waypoint import Waypoint


load_dotenv()

TOKEN: str = os.getenv("TOKEN")
BASE_URL: str = "https://api.spacetraders.io/v2/"


def register(symbol: str = "ROCINANTE--", faction: str = "GALACTIC"):
    result = requests.post(
        BASE_URL + "register",
        {"faction": faction, "symbol": symbol},
        timeout=30,
    )
    print(result)
    result = result.json()
    pprint(result)
    return result


class ClientMeta:
    def __init__(self, token: str = TOKEN, base_url: str = BASE_URL):
        self.token: str = token
        self.base_url: str = base_url

    def get_request(self, path: str, log: bool = False):
        try:
            response = requests.get(
                self.base_url + path,
                headers={"Authorization": f"Bearer {self.token}"},
                timeout=30,
            )

            if log:
                print(response)
                pprint(response.json())

            if response.status_code == 204:
                return {}

            result_body = response.json()

            if isinstance(result_body, dict):
                return result_body.get("data")

            return result_body

        except Exception as err:
            log(f"ERROR :: {err}")
            return {}

    def post_request(self, path: str, body=None, log: bool = None):
        if not body:
            body = {}

        try:
            response = requests.post(
                self.base_url + path,
                body,
                headers={"Authorization": f"Bearer {self.token}"},
                timeout=30,
            )

            if log:
                print(response)
                pprint(response.json())

            return response.json().get("data")

        except Exception as err:
            log(f"ERROR :: {err}")
            return {}


class FactionsClient(ClientMeta):
    def __init__(self):
        super().__init__()

    def all(self):
        return self.get_request("factions")

    def get(self, faction_symbol: str):
        return self.get_request(f"factions/{faction_symbol}")


class WaypointsClient(ClientMeta):
    def __init__(self):
        super().__init__()

    def all(self, system_symbol: str):
        return self.get_request(f"systems/{system_symbol}/waypoints")

    def get(self, system_symbol: str, waypoint_symbol: str):
        return Waypoint(
            **self.get_request(f"systems/{system_symbol}/waypoints/{waypoint_symbol}"),
            client=Client(),
        )

    def market(self, system_symbol: str, waypoint_symbol: str):
        return self.get_request(
            f"systems/{system_symbol}/waypoints/{waypoint_symbol}/market"
        )

    def shipyard(self, system_symbol: str, waypoint_symbol: str):
        return self.get_request(
            f"systems/{system_symbol}/waypoints/{waypoint_symbol}/shipyard"
        )

    def jumpgate(self, system_symbol: str, waypoint_symbol: str):
        return self.get_request(
            f"systems/{system_symbol}/waypoints/{waypoint_symbol}/jump-gate"
        )


class SystemsClient(ClientMeta):
    def __init__(self):
        super().__init__()
        self.waypoints: WaypointsClient = WaypointsClient()

    def full_list(self):
        return self.get_request("systems.json")

    def all(self):
        return [System(**system) for system in self.get_request("systems")]

    def get(self, system_symbol: str):
        return System(**self.get_request(f"systems/{system_symbol}"))


class MyShipsClient(ClientMeta):
    def __init__(self):
        super().__init__()

    def all(self):
        return [Ship(**ship, client=Client()) for ship in self.get_request("my/ships")]

    def get(self, ship_symbol: str):
        return Ship(**self.get_request(f"my/ships/{ship_symbol}"), client=Client())

    def cargo(self, ship_symbol: str):
        return ShipCargo(**self.get_request(f"my/ships/{ship_symbol}/cargo"))

    def nav(self, ship_symbol: str):
        return ShipNav(**self.get_request(f"my/ships/{ship_symbol}/nav"))

    def cooldown(self, ship_symbol: str):
        return self.get_request(f"my/ships/{ship_symbol}/cooldown")

    def orbit(self, ship_symbol: str):
        result = self.post_request(f"my/ships/{ship_symbol}/orbit")
        return ShipNav(**result.get("nav"))

    def dock(self, ship_symbol: str):
        response = self.post_request(f"my/ships/{ship_symbol}/dock")
        nav = ShipNav(**response.get("nav"))
        return nav

    def refine(self, ship_symbol: str):
        return self.post_request(f"my/ships/{ship_symbol}/refine")

    def chart(self, ship_symbol: str):
        return self.post_request(f"my/ships/{ship_symbol}/chart")

    def survey(self, ship_symbol: str):
        return self.post_request(f"my/ships/{ship_symbol}/survey")

    def extract(self, ship_symbol: str):
        return self.post_request(f"my/ships/{ship_symbol}/extract")

    def jettison(self, ship_symbol: str, trade_symbol: str, units: int):
        return self.post_request(
            f"my/ships/{ship_symbol}/jettison",
            {"symbol": trade_symbol, "units": units},
        )

    def jump(self, ship_symbol: str, system_symbol: str):
        return self.post_request(
            f"my/ships/{ship_symbol}/jump", {"systemSymbol": system_symbol}
        )

    def navigate(self, ship_symbol: str, waypoint_symbol: str):
        return self.post_request(
            f"my/ships/{ship_symbol}/navigate",
            {"waypointSymbol": waypoint_symbol},
        )

    def warp(self, ship_symbol: str):
        return self.post_request(f"my/ships/{ship_symbol}/warp", {})

    def sell(self, ship_symbol: str, trade_symbol: str, units: int):
        return self.post_request(
            f"my/ships/{ship_symbol}/sell",
            {"symbol": trade_symbol, "units": int(units)},
        )

    def purchase(self, ship_type: str, waypoint_symbol: str):
        return self.post_request(
            "my/ships",
            {"shipType": ship_type, "waypointSymbol": waypoint_symbol},
        )

    def scan_systems(self, ship_symbol: str):
        return self.post_request(f"my/ships/{ship_symbol}/scan/systems")

    def scan_waypoints(self, ship_symbol: str):
        return self.post_request(f"my/ships/{ship_symbol}/scan/waypoints")

    def scan_ships(self, ship_symbol: str):
        return self.post_request(f"my/ships/{ship_symbol}/scan/ships")

    def refuel(self, ship_symbol: str):
        return self.post_request(f"my/ships/{ship_symbol}/refuel")

    def purchase_cargo(self, ship_symbol: str, trade_symbol: str, units: int):
        return self.post_request(
            f"my/ships/{ship_symbol}/purchase", {"symbol": trade_symbol, "units": units}
        )

    def transfer_cargo(self, ship_symbol: str, trade_symbol: str, units: int):
        return self.post_request(
            f"my/ships/{ship_symbol}/transfer",
            {"tradeSymbol": trade_symbol, "units": units, "shipSymbol": ship_symbol},
        )


class MyContractsClient(ClientMeta):
    def __init__(self):
        super().__init__()

    def all(self):
        return [
            Contract(**contract, client=Client())
            for contract in self.get_request("my/contracts")
        ]

    def get(self, contract_id: str):
        return Contract(
            **self.get_request(f"my/contracts/{contract_id}"), client=Client()
        )

    def accept(self, contract_id: str):
        return self.post_request(f"my/contracts/{contract_id}/accept")

    def deliver(
        self, ship_symbol: str, contract_id: str, trade_symbol: str, units: int
    ):
        return self.post_request(
            f"my/contracts/{contract_id}/deliver",
            {
                "shipSymbol": ship_symbol,
                "tradeSymbol": trade_symbol,
                "units": units,
            },
        )

    def fulfill(self, contract_id: str):
        return self.post_request(
            f"my/contracts/{contract_id}/fulfill",
        )


class MyClient(ClientMeta):
    def __init__(self):
        super().__init__()
        self.ships: MyShipsClient = MyShipsClient()
        self.contracts: MyContractsClient = MyContractsClient()

    def agent(self):
        return Agent(**self.get_request("my/agent"))


class Client(ClientMeta):
    def __init__(self):
        super().__init__()
        self.my: MyClient = MyClient()
        self.factions: FactionsClient = FactionsClient()
        self.systems: SystemsClient = SystemsClient()
