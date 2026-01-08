import pandas as pd
from datetime import datetime

def run_habit_tracker():
    try:
        workouts = pd.read_csv("data/workouts.csv")
    except:
        workouts = pd.DataFrame(columns=["date"])

    today = datetime.now().strftime("%Y-%m-%d")
    workouts.loc[len(workouts)] = [today]
    workouts.to_csv("data/workouts.csv", index=False)

    last_7_days = workouts.tail(7)

    print("Workout days in last 7 days:", len(last_7_days))

    if len(last_7_days) < 3:
        print("Motivation Alert: You are skipping workouts!")
    else:
        print("Good job! Keep the consistency.")
