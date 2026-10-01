import pandas as pd


CHARGERS = {
    "Station_A": 2,
    "Station_B": 1,
    "Station_C": 2
}


def analyze_charging(df):

    results = []

    for _, vehicle in df.iterrows():

        location = vehicle["current_location"]
        battery = vehicle["battery_percent"]
        route = vehicle["next_route_km"]

        available_chargers = CHARGERS.get(location, 0)

        if battery <= 40 or route >= 80:
            charging_needed = "YES"
        else:
            charging_needed = "NO"

        if charging_needed == "YES" and available_chargers > 0:
            charger_status = "AVAILABLE"
            action = "Assign Charger"

        elif charging_needed == "YES":
            charger_status = "NOT AVAILABLE"
            action = "Wait for Charger"

        else:
            charger_status = "NOT REQUIRED"
            action = "No Charging Needed"

        results.append({
            "vehicle_id": vehicle["vehicle_id"],
            "location": location,
            "battery_percent": battery,
            "route_km": route,
            "chargers": available_chargers,
            "charging_needed": charging_needed,
            "charger_status": charger_status,
            "action": action
        })

    return pd.DataFrame(results)