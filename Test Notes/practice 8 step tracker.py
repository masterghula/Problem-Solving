def update_steps(steps_tracker, user, steps):
    """Updates the step count for a user."""
    if user in steps_tracker:
        steps_tracker[user] += steps  # Blank 1
    else:
        steps_tracker[user] = steps

def display_steps(steps_tracker):
    """Displays the step count for all users."""
    if steps_tracker:
        print("Daily Step Counts:")
        for user, steps in steps_tracker.items():  # Blank 2
            print(f"{user}: {steps} steps")
    else:
        print("No step counts recorded yet")  # Blank 3

# Create an empty steps tracker dictionary
steps_tracker = {}  # Blank 4

# Add or update steps for users
update_steps(steps_tracker, 'Alice', 5000)
update_steps(steps_tracker, 'Bob', 7000)
update_steps(steps_tracker, 'Alice', 2000)

# Display the step counts
display_steps(steps_tracker)  # Blank 5

# Check if a user has reached the daily goal
daily_goal = 10000
if steps_tracker['Bob'] >= daily_goal:  # Blank 6
    print("Bob has reached the daily step goal!")
