import pandas as pd


def analyze_routes(df):
    results = []

    for _, vehicle in df.iterrows():
        battery = vehicle["battery_percent"]
        route = vehicle["next_route_km"]

        if route >= 80 and battery <= 40:
            priority = "CRITICAL"
            action = "Charge Before Long Route"

        elif route >= 60 and battery <= 50:
            priority = "HIGH"
            action = "Charging Recommended"

        elif route >= 40:
            priority = "MEDIUM"
            action = "Monitor Battery"

        else:
            priority = "LOW"
            action = "No Immediate Action"

        results.append({
            "vehicle_id": vehicle["vehicle_id"],
            "battery_percent": battery,
            "route_km": route,
            "priority": priority,
            "action": action
        })

    return pd.DataFrame(results)