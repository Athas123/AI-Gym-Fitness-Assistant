import pandas as pd
import matplotlib.pyplot as plt

def run_performance_analyzer():
    try:
        workouts = pd.read_csv("data/workouts.csv")
    except:
        print("No workout data found")
        return

    workout_count = len(workouts)

    score = min(100, workout_count * 15)

    print("Performance Score:", score)

    plt.bar(["Performance"], [score])
    plt.ylim(0, 100)
    plt.title("Weekly Performance Score")
    plt.savefig("outputs/performance_score.png")
    plt.close()
