

import os
from datetime import datetime
from time import sleep
from typing import List
from pprint import pprint, pformat
from pydash import find

from dotenv import load_dotenv
import requests

from agent import Agent
from contract import Contract

load_dotenv()

TOKEN = os.getenv("TOKEN")

class Client:
    token: str = TOKEN
    base_url: str = "https://api.spacetraders.io/v2/"
    agent: Agent
    contracts: List
    factions: List
    ships: List
    systems: List
        
    def log(message: str) -> None:
        print("[" + datetime.now().isoformat()[:19] + "] :: " + message)

    def get(path: str, log: bool = False):
        try:
            response = requests.get(
                self.base_url + path, headers={"Authorization": f"Bearer {self.token}"}, timeout=30
            )

            if (log):
                log(str(response))
                log(pformat(response.json()))

            if response.status_code == 204:
                return {}

            return response.json().get("data")

        except Exception as err:
            log(f"ERROR :: {err}")
            return {}
        
    def post(path: str, body=None, log=None):
        if not body:
            body = {}

        try:
            response = requests.post(
                self.base_url + path,
                body,
                headers={"Authorization": f"Bearer {self.token}"},
                timeout=30,
            )

            if (log):
                log(str(response))
                log(pformat(response.json()))

            return response.json().get("data")

        except Exception as err:
            log(f"ERROR :: {err}")
            return {}

    # AGENT
    def my_agent(self):
        agent = self.get("my/agent")
        self.agent = Agent(**agent)
        pprint(agent)
        return agent

    # FACTIONS
    def factions(self):
        factions = self.get("factions")
        self.factions = factions
        pprint(factions)
        return factions

    def faction(self, faction_symbol: str):
        faction = self.get(f"factions/{faction_symbol}")
        pprint(faction)
        return faction
        
    # SHIPS
    def my_ships(self):
        ships = self.get("my/ships")
        self.ships = ships
        return ships

    def get_ship(self, ship_symbol: str):
        ship = self.get(f"my/ships/{ship_symbol}")
        return ship

    def get_ship_cargo(self, ship_symbol: str):
        cargo = self.get(f"my/ships/{ship_symbol}/cargo")
        return cargo
    
    def get_ship_nav(self, ship_symbol: str):
        nav = self.get(f"my/ships/{ship_symbol}/nav")
        return nav
    
    def get_ship_cooldown(self, ship_symbol: str):
        coooldown = self.get(f"my/ships/{ship_symbol}/cooldown")
        return coooldown

    def ship_orbit(self, ship_symbol: str):
        response = self.post(f"my/ships/{ship_symbol}/orbit")
        print(f"{response.get('nav') = }")
        self.log(ship_symbol + f" orbiting {self.nav.get('waypointSymbol')}")

    def ship_dock(self, ship_symbol: str):
        response = self.post(f"my/ships/{ship_symbol}/dock")
        print(f"{response.get('nav') = }")

        nav = response.get("nav")
        if nav:
            # self.nav = nav
            self.log(ship_symbol + f" docked at {nav.get('waypointSymbol')}")
        
        else:
            sleep(5)
            self.ship_dock(ship_symbol)

    def ship_refine(self, ship_symbol: str):
        response = self.post(f"my/ships/{ship_symbol}/refine")
        pprint(response)

    def ship_chart(self, ship_symbol: str):
        response = self.post(f"my/ships/{ship_symbol}/chart")
        pprint(response)

    def ship_survey(self, ship_symbol: str):
        response = self.post(f"my/ships/{ship_symbol}/survey")
        pprint(response)

    def ship_extract(self, ship_symbol: str):
        response = self.post(f"my/ships/{ship_symbol}/extract")
        self.cargo = response.get("cargo")
        extraction = response.get('extraction', {})
        self.log(self.symbol + f" extracted: {extraction.get('yield')}")
        pprint(response)

    def ship_jettison(self, ship_symbol: str):
        response = self.post(f"my/ships/{ship_symbol}/jettison")
        pprint(response)

    def ship_jump(self, ship_symbol: str):
        response = self.post(f"my/ships/{ship_symbol}/jump")
        pprint(response)

    def ship_navigate(self, ship_symbol: str, waypoint_symbol: str):
        response = self.post(f"my/ships/{ship_symbol}/navigate", {"waypointSymbol": waypoint_symbol})
        pprint(response)
        nav = response["nav"]
        fuel = response["fuel"]
        pprint(nav)
        pprint(fuel)
        self.log(
            self.symbol
            + f" in transit to {self.nav.get('route').get('destination').get('symbol')}"
        )

    def ship_warp(self, ship_symbol: str):
        response = self.post(f"my/ships/{ship_symbol}/warp", {})
        pprint(response)

    def ship_sell(self, ship_symbol: str, agent, trade_symbol: str, units: int):
        result = self.post(
            f"my/ships/{ship_symbol}/sell",
            {"symbol": trade_symbol, "units": int(units)},
        )

        agent.credits = result["agent"]["credits"]
        cargo = result["cargo"]

        transaction = result["transaction"]
        response = {
            "symbol": transaction.get("tradeSymbol"),
            "units": transaction.get("units"),
            "total": transaction.get("totalPrice"),
            "pricePerUnit": transaction.get("pricePerUnit"),
        }

        self.log(ship_symbol + f" sold: {pformat(response)}")
        sleep(.5)
        return result["transaction"]

    def ships_purchase(self, ship_type: str, waypoint: str):
        result = self.post("my/ships", {"shipType": ship_type, "waypointSymbol": waypoint})
        pprint(result)
        return result

    def ship_scan_systems(self, ship_symbol: str):
        response = self.post(f"my/ships/{ship_symbol}/scan/systems")
        systems = response.get("systems")
        cooldown = response.get("cooldown")
        print(f"{cooldown = }")
        print(f"{systems = }")
        return systems
    
    def ship_scan_waypoints(self, ship_symbol: str):
        response = self.post(f"my/ships/{ship_symbol}/scan/waypoints")
        waypoints = response.get("waypoints")
        cooldown = response.get("cooldown")
        print(f"{cooldown = }")
        print(f"{waypoints = }")
        return waypoints
    
    def ship_scan_ships(self, ship_symbol: str):
        response = self.post(f"my/ships/{ship_symbol}/scan/ships")
        ships = response.get("ships")
        cooldown = response.get("cooldown")
        print(f"{cooldown = }")
        print(f"{ships = }")
        return ships
    
    def ship_refuel(self, ship_symbol: str):
        result = self.post(f"my/ships/{ship_symbol}/refuel")
        fuel = result["fuel"]
        
        credits_ = result.get("agent").get("credits")
        print(f"{fuel = }")
        print(f"{credits_ = }")

        self.log(ship_symbol + " refueled")

    def ship_purchase_cargo(self, ship_symbol: str, trade_symbol: str, units: int):
        result = self.post(f"my/ships/{ship_symbol}/purchase",{"symbol": trade_symbol, "units": units})
        credits_ = result.get("agent").get("credits")
        cargo  = result["cargo"]
        transaction  = result["transaction"]

        print(f"{credits_ = }")
        print(f"{cargo = }")
        print(f"{transaction = }")

        self.log(ship_symbol + " cargo purchased")

    def ship_transfer_cargo(self, ship_symbol: str, trade_symbol: str, units: int):
        result = self.post(f"my/ships/{ship_symbol}/transfer",{"tradeSymbol": trade_symbol, "units": units, "shipSymbol": ship_symbol})
        cargo  = result["cargo"]
        print(f"{cargo = }")

        self.log(ship_symbol + " cargo transfered")

    # CONTRACTS
    def my_contracts(self):
        contracts = self.get("my/contracts")
        self.contracts = contracts
        return contracts

    def contract(self, contract_id: str):
        contract = self.get(f"my/contracts/{contract_id}")
        return Contract(**contract)
    
    def contract_accept(self, contract_id: str):
        response = self.post(f"my/contracts/{contract_id}/accept")
        agent = response.get("agent")
        contract = response.get("contract")

        print(f"{agent = }")
        print(f"{contract = }")
        return response
    
    def contract_deliver(self, ship, contract_id: str):
        trade_symbol = self.terms.get("deliver")[0].get("tradeSymbol")
        trade_good = find(
            ship.cargo.get("inventory"),
            lambda good: good.get("symbol") == trade_symbol,
        )
        units = trade_good.get("units")

        result = self.post(
            f"my/contracts/{contract_id}/deliver",
            {
                "shipSymbol": ship.symbol,
                "tradeSymbol": trade_symbol,
                "units": units,
            },
        )

        ship.cargo = result.get("cargo")
        terms = result.get("contract").get("terms")
        print(f"{terms = }")
        self.log(str(units) + " " + trade_symbol + " delivered")
        self.log("Fulfilled: " + str(self.terms.get("deliver")[0].get("unitsFulfilled", 0)))

        return result

    def contract_fulfill(self, contract_id: str):
        result = self.post(
            f"my/contracts/{contract_id}/fulfill",
        )

        agent  = result.get("agent")
        contract  = result.get("contract")

        print(f"{agent = }")
        print(f"{contract = }")

        return result

    # SYSTEMS
    def systems(self):
        systems = self.get("systems")
        self.systems = systems
        return systems

    def system(self, system_symbol: str):
        pass

    # WAYPOINTS
    def waypoints(self, system_symbol: str):
        waypoints = self.get(f"systems/{system_symbol}/waypoints")
        print(f"{waypoints = }")
        return waypoints

    def waypoint(self, waypoint_symbol: str):
        pass    

    def waypoint_market(self):
        pass

    def waypoint_shipyard(self):
        pass

    def waypoint_jump_gate(self):
        pass

