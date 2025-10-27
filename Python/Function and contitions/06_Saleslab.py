# ---------------------------------------------
# Activity: Functions
# ---------------------------------------------
# This script walks through all tasks:
# 1. Analyze a basic function
# 2. Add parameters and calculations
# 3. Refine the function with two parameters
# 4. Test it with different values
# ---------------------------------------------

# Task 1: Analyze a function (basic structure)
def total_sales():
    # Placeholder function (initial step)
    # Originally had no parameters or logic
    return


# Task 2a: Add a calculation (1 parameter)
def total_sales(n):
    """Return total sales for n tickets at $7.99 each."""
    return n * 7.99


# Task 2b: Test the 1-parameter version
print("Task 2 - Testing total_sales(n):")
print("Total sales for 59 tickets:", total_sales(59))  # Expected: 471.41
print("-" * 40)


# Task 3a: Refine the function (2 parameters)
def total_sales(price, num_tickets):
    """
    Return total sales for given ticket price and number of tickets.
    Rounds the result to 2 decimal places.
    """
    total = price * num_tickets
    return round(total, 2)


# Task 3b: Test the 2-parameter version
print("Task 3 - Testing total_sales(price, num_tickets):")
print("Total sales (15.99, 1001):", total_sales(15.99, 1001))  # Expected: 16005.99
print("-" * 40)


# Task 4: Test with multiple values
print("Task 4 - Testing different scenarios:")
print("Total sales (16.99, 1232):", total_sales(16.99, 1232))  # Expected: 20931.68
print("Total sales (10.50, 1472):", total_sales(10.50, 1472))  # Expected: 15456.00
print("Total sales (5.00, 349):", total_sales(5.00, 349))      # Expected: 1745.00
print("-" * 40)

print("All tasks completed successfully!")
