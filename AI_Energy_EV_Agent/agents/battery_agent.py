import pandas as pd


def analyze_battery(df):
    results = []

    for _, vehicle in df.iterrows():

        battery = vehicle["battery_percent"]

        if battery <= 20:
            priority = "CRITICAL"
            action = "Charge Immediately"

        elif battery <= 40:
            priority = "HIGH"
            action = "Schedule Charging"

        elif battery <= 60:
            priority = "MEDIUM"
            action = "Charging Can Be Scheduled"

        else:
            priority = "LOW"
            action = "No Immediate Charging"

        results.append({
            "vehicle_id": vehicle["vehicle_id"],
            "battery_percent": battery,
            "priority": priority,
            "action": action
        })

    return pd.DataFrame(results)