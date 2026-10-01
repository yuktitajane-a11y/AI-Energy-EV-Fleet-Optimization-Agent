import pandas as pd


def get_price(time):
    if time >= "23:00":
        return 5
    elif time >= "18:00":
        return 12
    elif time >= "10:00":
        return 10
    else:
        return 6


def analyze_cost(df):

    results = []

    for _, vehicle in df.iterrows():

        battery = vehicle["battery_percent"]
        capacity = vehicle["battery_capacity_kwh"]
        departure = vehicle["departure_time"]

        # Energy required to fully charge
        energy_needed = capacity * (100 - battery) / 100

        # Electricity price
        price = get_price(departure)

        # Charging cost
        charging_cost = energy_needed * price

        results.append({
            "vehicle_id": vehicle["vehicle_id"],
            "battery_percent": battery,
            "capacity_kwh": capacity,
            "departure_time": departure,
            "energy_needed_kwh": round(energy_needed, 2),
            "price_per_kwh": price,
            "charging_cost": round(charging_cost, 2)
        })

    return pd.DataFrame(results)