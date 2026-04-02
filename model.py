import pandas as pd

def recommend_trip(data, interest, budget):
    
    # Step 1: Filter by interest
    filtered = data[data["Interest"].str.lower() == interest.lower()]

    if filtered.empty:
        filtered = data.copy()

    # Step 2: Budget range filter (±30%)
    lower = budget * 0.7
    upper = budget * 1.2

    budget_filtered = filtered[
        (filtered["Price"] >= lower) & (filtered["Price"] <= upper)
    ]

    if budget_filtered.empty:
        budget_filtered = filtered

    budget_filtered = budget_filtered.copy()

    # Step 3: Rank by closeness to budget
    budget_filtered["Score"] = abs(budget_filtered["Price"] - budget)

    result = budget_filtered.sort_values(by="Score")

    return result.head(3).drop(columns=["Score"])


def suggest_vehicle(distance, budget):
    if distance < 200:
        return "🚗 Car"
    elif distance < 800:
        return "🚌 Bus / 🚆 Train"
    else:
        if budget > 10000:
            return "✈ Flight"
        else:
            return "🚆 Train"