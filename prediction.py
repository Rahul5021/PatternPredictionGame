import tkinter as tk
import random

# Define a dictionary of pattern rules, where the key is the pattern name and the value is a function to generate the
# next number


pattern_rules = {
    "Increasing Sequence": lambda pattern: pattern + [pattern[-1] + 1],
    "Even Numbers": lambda pattern: pattern + [pattern[-1] + 2],
    "Fibonacci Sequence": lambda pattern: pattern + [pattern[-1] + pattern[-2]] if len(pattern) >= 2 else pattern + [1],
    "Prime Numbers": lambda pattern: pattern + [next_prime(pattern[-1])],
    "Geometric Sequence": lambda pattern: pattern + [pattern[-1] * 2],
    "Reverse Order": lambda pattern: pattern + [pattern[-1] - 1],
    "Square Numbers": lambda pattern: pattern + [(int(pattern[-1]**0.5) + 1)**2],
    "Power of Two": lambda pattern: pattern + [pattern[-1] * 2],
    "Arithmetic Progression": lambda pattern, common_difference: pattern + [pattern[-1] + common_difference],
    "Exponential Growth": lambda pattern, growth_factor: pattern + [pattern[-1] * growth_factor],
    "Triangular Numbers": lambda pattern: pattern + [pattern[-1] + len(pattern) + 1],
    # Add more pattern rules here
}

# Function to find the next prime number
def next_prime(n):
    n += 1
    while True:
        if is_prime(n):
            return n
        n += 1

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Initialize pattern
current_pattern = []
current_pattern_name = ""

# Generate a new random pattern
# Generate a new random pattern
def generate_pattern():
    global current_pattern, current_pattern_name
    current_pattern_name = random.choice(list(pattern_rules.keys()))
    if current_pattern_name == "Arithmetic Progression":
        common_difference = random.randint(1, 5)  # You can adjust the range as needed
        current_pattern = pattern_rules[current_pattern_name](current_pattern, common_difference)
    elif current_pattern_name == "Exponential Growth":
        growth_factor = random.uniform(1.1, 2.0)  # You can adjust the range as needed
        current_pattern = pattern_rules[current_pattern_name](current_pattern, growth_factor)
    else:
        current_pattern = [random.randint(1, 10)]  # Start with a random number
        while len(current_pattern) < 6:
            current_pattern = pattern_rules[current_pattern_name](current_pattern)
    pattern_label.config(text=f"Pattern: {', '.join(map(str, current_pattern[:-1]))}")
    feedback_label.config(text="")
    feedback_label.config(fg="black")  # Reset text color to black


# Check the user's prediction
def check_prediction():
    user_input = prediction_entry.get()
    try:
        user_input = int(user_input)
        next_number = current_pattern[-1]
        if user_input == next_number:
            feedback_label.config(text="Correct! You predicted it.", fg="green")  # Set text color to green
        else:
            feedback_label.config(text="Incorrect. Try again.", fg="red")  # Set text color to red
    except ValueError:
        feedback_label.config(text="Invalid input. Please enter a number.", fg="red")  # Set text color to red

# Create the main window
window = tk.Tk()
window.title("Pattern Game")
window.geometry("400x250")  # Set window size

# Create a label to display the current pattern
pattern_label = tk.Label(window, text="Pattern: ", font=("Helvetica", 14))
pattern_label.pack()

# Create an entry widget for the user to input their prediction
prediction_entry = tk.Entry(window, font=("Helvetica", 12))
prediction_entry.pack()

# Create a button to check the prediction
check_button = tk.Button(window, text="Check Prediction", command=check_prediction, font=("Helvetica", 12))
check_button.pack()

# Create a button to generate the next pattern
next_button = tk.Button(window, text="Next", command=generate_pattern, font=("Helvetica", 12))
next_button.pack()

# Create a label to display feedback
feedback_label = tk.Label(window, text="", font=("Helvetica", 12))
feedback_label.pack()

# Initialize the pattern
generate_pattern()

# Start the main loop
window.mainloop()
