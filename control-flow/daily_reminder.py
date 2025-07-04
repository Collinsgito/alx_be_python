# Daily Task Reminder System
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Please schedule time for it today.")
    case "medium":
        if time_bound == "yes":
            print(f"Note: '{task}' is a medium priority task with a deadline. Try to complete it soon.")
        else:
            print(f"Note: '{task}' is a medium priority task. Consider completing it this week.")
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority task with some time constraints. No rush, but don't forget.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level entered. Please use high, medium, or low.")

print("Well done on completing this project! Let the world hear about this milestone achieved.")

