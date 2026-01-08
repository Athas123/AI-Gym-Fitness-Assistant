import pandas as pd
from datetime import datetime

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

def calculate_calories(weight, goal):
    maintenance = 24 * weight
    if goal == "weight_loss":
        return maintenance - 500
    elif goal == "weight_gain":
        return maintenance + 500
    else:
        return maintenance

def diet_suggestion(bmi):
    if bmi > 25:
        return "Low carb, high fiber diet"
    elif bmi < 18:
        return "High protein, calorie surplus diet"
    else:
        return "Balanced diet"

def run_dietician():
    users = pd.read_csv("data/users.csv")
    user = users.iloc[0]

    bmi = calculate_bmi(user["weight_kg"], user["height_cm"])
    calories = calculate_calories(user["weight_kg"], user["goal"])
    diet = diet_suggestion(bmi)

    log = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "bmi": bmi,
        "calories": calories,
        "diet": diet
    }

    df = pd.DataFrame([log])
    df.to_csv("data/diet_logs.csv", mode="a", header=False, index=False)

    print("BMI:", bmi)
    print("Daily Calories:", calories)
    print("Diet Plan:", diet)
