import pandas as pd

from agents.battery_agent import analyze_battery
from agents.route_agent import analyze_routes
from agents.charging_agent import analyze_charging
from agents.cost_agent import analyze_cost
from agents.optimization_agent import optimize_fleet
from agents.recommendation_agent import generate_recommendations


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

    print("\n===== CHARGING AGENT =====")
    charging_result = analyze_charging(df)
    print(charging_result.to_string(index=False))

    print("\n===== COST AGENT =====")
    cost_result = analyze_cost(df)
    print(cost_result.to_string(index=False))

    print("\n===== OPTIMIZATION AGENT =====")
    optimization_result = optimize_fleet(
        df,
        battery_result,
        route_result,
        charging_result,
        cost_result
    )
    print(optimization_result.to_string(index=False))

    print("\n===== RECOMMENDATION AGENT =====")
    recommendation_result = generate_recommendations(
        optimization_result
    )
    print(recommendation_result.to_string(index=False))


if __name__ == "__main__":
    main()