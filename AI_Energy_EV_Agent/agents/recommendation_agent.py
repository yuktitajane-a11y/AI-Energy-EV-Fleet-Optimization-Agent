import pandas as pd


def generate_recommendations(optimization_result):

    results = []

    for _, row in optimization_result.iterrows():

        vehicle_id = row["vehicle_id"]
        decision = row["final_decision"]

        if decision == "CHARGE NOW":
            recommendation = "Charge immediately"

        elif decision == "CHARGE BEFORE ROUTE":
            recommendation = "Charge before route"

        elif decision == "SCHEDULE CHARGING":
            recommendation = "Schedule charging"

        else:
            recommendation = "No charging required"

        results.append({
            "vehicle_id": vehicle_id,
            "decision": decision,
            "recommendation": recommendation
        })

    return pd.DataFrame(results)