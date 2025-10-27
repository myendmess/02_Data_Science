# Define a function that checks validity of username based on length.
def hint_username(username):
    if len(username) < 8:
        return "Invalid username. Must be at least 8 characters long."
    elif len(username) > 15:
        return "Invalid username. Cannot exceed 15 characters."
    else:
        return "Valid username."

# Define a function that uses modulo to check if a number is even.
def is_even(number):
    return number % 2 == 0

# Ask the user to input a username
username_input = input("Enter your username: ")

# Validate username
print(hint_username(username_input))




