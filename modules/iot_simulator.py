import random

def run_iot_simulator():
    heart_rate = random.randint(60, 140)
    load = random.randint(10, 50)

    print("Heart Rate:", heart_rate)
    print("Current Load:", load, "kg")

    if heart_rate > 120:
        print("AI Suggestion: Reduce intensity and take rest")
    else:
        print("AI Suggestion: You can increase intensity safely")
