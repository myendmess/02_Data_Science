# ---------------------------------------------
# Activity: Conditional Statements
# ---------------------------------------------
# In this lab, you will define a function that determines
# whether a customer should receive a marketing email,
# and if applicable, a coupon as well.
# ---------------------------------------------


# ✅ Task 1: Define a comparator function
def send_email(num_visits, visits_email):
    """Decide whether to send a marketing email based on number of visits."""
    if num_visits >= visits_email:
        print("Send email.")
    else:
        print("Not enough visits.")


# Test Task 1
print("Task 1 tests:")
send_email(num_visits=3, visits_email=5)    # Expected: Not enough visits.
send_email(num_visits=5, visits_email=5)    # Expected: Send email.
send_email(num_visits=15, visits_email=10)  # Expected: Send email.
print("-" * 40)


# ✅ Task 2: Add logical branching (email + coupon)
def send_email(num_visits, visits_email, visits_coupon):
    """
    Decide whether to send an email or an email with a coupon
    based on how many times a customer visited the theater.
    """
    if num_visits >= visits_coupon:
        print("Send email with coupon.")
    elif num_visits >= visits_email:
        print("Send email only.")
    else:
        print("Not enough visits.")


# Test Task 2
print("Task 2 tests:")
send_email(num_visits=3, visits_email=5, visits_coupon=8)   # Not enough visits.
send_email(num_visits=5, visits_email=5, visits_coupon=8)   # Send email only.
send_email(num_visits=6, visits_email=5, visits_coupon=8)   # Send email only.
send_email(num_visits=8, visits_email=5, visits_coupon=8)   # Send email with coupon.
send_email(num_visits=10, visits_email=5, visits_coupon=8)  # Send email with coupon.
print("-" * 40)

print("All tests completed successfully!")
