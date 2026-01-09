from modules.dietician import run_dietician
from modules.habit_tracker import run_habit_tracker
from modules.performance_analyzer import run_performance_analyzer
from modules.virtual_buddy import run_virtual_buddy
from modules.recommender import run_gym_recommender
from modules.iot_simulator import run_iot_simulator

def main():
    print("AI Gym & Fitness Assistant Started")

    print("\n--- Dietician Module ---")
    run_dietician()

    print("\n--- Habit Tracker Module ---")
    run_habit_tracker()

    print("\n--- Performance Analyzer ---")
    run_performance_analyzer()

    print("\n--- Virtual Gym Buddy ---")
    run_virtual_buddy()

    print("\n--- Gym Recommender & Planner ---")
    run_gym_recommender()

    print("\n--- Smart Gym Assistant (IoT Simulation) ---")
    run_iot_simulator()

if __name__ == "__main__":
    main()
