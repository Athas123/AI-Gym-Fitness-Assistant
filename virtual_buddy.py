def run_virtual_buddy():
    print("\nVirtual Gym Buddy Activated")

    print("How are you feeling today?")
    print("1. Motivated")
    print("2. Tired")
    print("3. Lazy")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        print("Awesome! Let's push your limits today 💪")
    elif choice == "2":
        print("It's okay to feel tired. Light workout and stretching recommended 🧘")
    elif choice == "3":
        print("No excuses! Start with a 10-minute workout 🚀")
    else:
        print("Invalid input. Stay consistent and keep moving!")
