# pylint: disable=cell-var-from-loop

from time import sleep
from pprint import pprint
from nicegui import ui
from pydash import find, map_, remove

from agent import Agent

agent = Agent()
ship = agent.get_ship(0)
contract = agent.get_contract(0)
system = agent.get_system()


@ui.refreshable
def ship_ui():
    def _refresh():
        ship_ui.refresh()

    def _update_cargo():
        ship.get_cargo()
        ship_ui.refresh()

    def _sell(resource):
        extraction = ship.sell(agent, resource.get("symbol"), resource.get("units"))
        symbol = extraction.get("tradeSymbol")
        units = extraction.get("units")
        price_per_unit = extraction.get("pricePerUnit")
        total_price = extraction.get("totalPrice")

        ui.notify(
            f"Sold: {units} {symbol} for {total_price} ({price_per_unit} per unit)"
        )

        ship_ui.refresh()
        contract_ui.refresh()

    def _extract():
        try:
            while True:
                ship.extract()
                if ship.cargo["units"] >= ship.cargo["capacity"]:
                    break

                sleep(70)

            ship_ui.refresh()

        except Exception:
            print("Cargo full")
            ship_ui.refresh()

    with ui.column().classes("w-1/5"):
        ui.button("Refresh", on_click=_refresh)
        ui.label(f"Ship: {ship.symbol}")
        ui.label(f"Crew Moral: {ship.crew['morale']}")
        ui.label(f"Engine Condition: {ship.engine['condition']}")
        ui.label(f"Frame Condition: {ship.frame['condition']}")
        ui.label(f"Reactor Condition: {ship.reactor['condition']}")
        ui.label(f"Fuel: {ship.fuel['current']} / {ship.fuel['capacity']}")
        ui.label(f"Storage: {ship.cargo['units']} / {ship.cargo['capacity']}")

        if ship.nav["status"] == "IN_ORBIT":
            ui.button("extract", on_click=_extract)
        ui.button("cooldown", on_click=lambda: ui.notify(ship.cooldown()))

        ui.label("Cargo")
        ui.button("Update Cargo", on_click=_update_cargo)
        inventory = ship.cargo["inventory"]
        sellable = remove(
            inventory,
            lambda resource: resource.get("name") not in ("Antimatter", "Aluminum Ore"),
        )

        for item in inventory:
            ui.label(f"{item.get('name')}: {item.get('units')}")

        map_(
            sellable,
            lambda item: ui.button(
                f"{item.get('name')}: {item.get('units')}",
                on_click=lambda: _sell(item),
            ),
        )


@ui.refreshable
def system_ui():
    def _dock():
        ship.dock()
        system_ui.refresh()
        ship_ui.refresh()

    def _orbit():
        ship.orbit()
        system_ui.refresh()
        ship_ui.refresh()

    def _refuel():
        ship.refuel(agent)
        system_ui.refresh()
        ship_ui.refresh()

    def _navigate(waypoint):
        ship.navigate(waypoint)
        system_ui.refresh()
        ship_ui.refresh()

    def _refresh():
        system_ui.refresh()

    with ui.column().classes("w-1/5"):
        ui.button("Refresh", on_click=_refresh)
        ui.label(f"System: {ship.nav['systemSymbol']}")
        ui.label(f"Waypoint: {ship.nav['waypointSymbol']}")
        ui.label(f"Status: {ship.nav['status']}")

        if ship.nav["status"] == "IN_ORBIT":
            ui.button("dock", on_click=_dock)
        if ship.nav["status"] == "DOCKED":
            ui.button("refuel", on_click=_refuel)
            ui.button("orbit", on_click=_orbit)

        if ship.nav["status"] == "IN_ORBIT":
            if ship.nav["waypointSymbol"] == "X1-DF55-20250Z":
                ui.button(
                    "navigate: X1-DF55-17335A",
                    on_click=lambda: _navigate("X1-DF55-17335A"),
                )
            else:
                ui.button(
                    "navigate: X1-DF55-20250Z",
                    on_click=lambda: _navigate("X1-DF55-20250Z"),
                )

            map_(
                system.waypoints,
                lambda waypoint: ui.button(
                    f"{waypoint.get('symbol')}: {waypoint.get('type')}",
                    on_click=lambda: _navigate(waypoint.get("symbol")),
                ),
            )


@ui.refreshable
def system_chart_ui():
    def _refresh():
        system_ui.refresh()

    with ui.column().classes("w-1/5"):
        ui.button("Refresh", on_click=_refresh)

        system_waypoints = map_(
            system.waypoints,
            lambda waypoint: {
                "name": waypoint.get("symbol"),
                "data": [{"x": waypoint.get("x"), "y": waypoint.get("y")}],
            },
        )
        system_waypoints.append(
            {
                "name": system.symbol,
                "data": [{"x": 0, "y": 0}],
            }
        )

        ui.chart(
            {
                "title": False,
                "chart": {"type": "scatter"},
                "legend": {"enabled": False},
                "yAxis": {"visible": False},
                "xAxis": {"visible": False},
                "series": system_waypoints,
            }
        ).classes("w-full h-64")

        ui.chart(
            {
                "title": False,
                "chart": {"type": "scatter"},
                "legend": {"enabled": False},
                "yAxis": {"visible": False},
                "xAxis": {"visible": False},
                "series": map_(
                    agent.systems(),
                    lambda system: {
                        "name": system.get("symbol"),
                        "data": [{"x": system.get("x"), "y": system.get("y")}],
                    },
                ),
            }
        ).classes("w-full h-64")


@ui.refreshable
def contract_ui():
    def _refresh():
        contract_ui.refresh()

    def _deliver():
        trade_symbol = contract.terms["deliver"][0]["tradeSymbol"]
        trade_inventory = find(
            ship.cargo["inventory"],
            lambda good: good.get("symbol") == trade_symbol,
        )

        print(ship.symbol, trade_symbol, trade_inventory.get("units"))
        # contract.deliver(ship.symbol, trade_symbol, trade_inventory.get("units"))

        contract_ui.refresh()
        ship_ui.refresh()

    with ui.column().classes("w-1/5"):
        ui.button("Refresh", on_click=_refresh)
        ui.label(f"Credits: {agent.credits}")
        ui.label(f"Contract: {contract.id_}")
        ui.label(f"Trade Symbol: {contract.terms['deliver'][0]['tradeSymbol']}")
        ui.label(f"Deadline: {contract.terms['deadline']}")
        ui.label(f"Required: {contract.terms['deliver'][0]['unitsRequired']}")
        ui.label(f"Fulfilled: {contract.terms['deliver'][0]['unitsFulfilled']}")
        if (
            contract.terms["deliver"][0]["destinationSymbol"]
            == ship.nav["waypointSymbol"]
        ):
            ui.button("deliver", on_click=_deliver)


if __name__ in {"__main__", "__mp_main__"}:
    ui.dark_mode().enable()

    with ui.row().classes("w-full"):
        ship_ui()
        system_ui()
        system_chart_ui()
        contract_ui()

    ui.run()
