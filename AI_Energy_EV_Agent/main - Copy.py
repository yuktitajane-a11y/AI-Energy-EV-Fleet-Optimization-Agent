import pandas as pd

from agents.battery_agent import analyze_battery
from agents.route_agent import analyze_routes


def main():

    df = pd.read_csv("data/ev_fleet.csv")

    print("\n===== EV FLEET DATA =====")
    print(df.to_string(index=False))

    print("\n===== BATTERY AGENT =====")
    battery_result = analyze_battery(df)
    print(battery_result.to_string(index=False))

    print("\n===== ROUTE AGENT =====")
    route_result = analyze_routes(df)
    print(route_result.to_string(index=False))


if __name__ == "__main__":
    main()