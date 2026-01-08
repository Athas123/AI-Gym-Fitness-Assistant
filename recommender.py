import pandas as pd

def run_gym_recommender():
    users = pd.read_csv("data/users.csv")
    user = users.iloc[0]

    city = user["city"]
    goal = user["goal"]

    print("City:", city)
    print("Fitness Goal:", goal)

    if goal == "weight_loss":
        plan = "Cardio-focused gym with HIIT programs"
        challenge = "10,000 steps daily challenge"
    elif goal == "weight_gain":
        plan = "Strength training gym with weight lifting"
        challenge = "Progressive overload challenge"
    else:
        plan = "Balanced fitness center"
        challenge = "Consistency challenge"

    print("Recommended Gym Type:", plan)
    print("Suggested Weekly Challenge:", challenge)
