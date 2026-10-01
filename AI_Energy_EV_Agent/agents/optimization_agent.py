import pandas as pd


def optimize_fleet(df, battery_result, route_result, charging_result, cost_result):

    results = []

    for _, vehicle in df.iterrows():

        vehicle_id = vehicle["vehicle_id"]

        battery = battery_result[
            battery_result["vehicle_id"] == vehicle_id
        ].iloc[0]

        route = route_result[
            route_result["vehicle_id"] == vehicle_id
        ].iloc[0]

        charging = charging_result[
            charging_result["vehicle_id"] == vehicle_id
        ].iloc[0]

        cost = cost_result[
            cost_result["vehicle_id"] == vehicle_id
        ].iloc[0]

        if (
            battery["priority"] in ["CRITICAL", "HIGH"]
            and charging["charger_status"] == "AVAILABLE"
        ):
            decision = "CHARGE NOW"

        elif (
            route["priority"] in ["CRITICAL", "HIGH"]
            and charging["charger_status"] == "AVAILABLE"
        ):
            decision = "CHARGE BEFORE ROUTE"

        elif battery["priority"] == "MEDIUM":
            decision = "SCHEDULE CHARGING"

        else:
            decision = "NO CHARGING NEEDED"

        results.append({
            "vehicle_id": vehicle_id,
            "battery_priority": battery["priority"],
            "route_priority": route["priority"],
            "charger_status": charging["charger_status"],
            "charging_cost": cost["charging_cost"],
            "final_decision": decision
        })

    return pd.DataFrame(results)
