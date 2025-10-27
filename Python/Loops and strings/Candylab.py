from time import sleep

# -------------------------------
# Task 1: Candy purchase counter
# -------------------------------
print("Task 1: Candy purchases")
candy_purchased = 0

while candy_purchased <= 5:
    print(f'Candy purchased: {candy_purchased}')
    candy_purchased += 1

print("\n")  # Just to separate output

# ----------------------------------------------
# Task 2: Candy purchase multiples of 10
# ----------------------------------------------
print("Task 2: Candy purchases every 10")
candy_purchased = 0

while candy_purchased <= 100:
    if candy_purchased % 10 == 0:
        print(f'Candy purchased: {candy_purchased}')
    candy_purchased += 1

print("\n")  # Separate output

# ----------------------------------------------
# Task 3: Webpage timer countdown
# ----------------------------------------------
print("Task 3: Reservation timer")
mins = 10

while mins >= 0:
    if mins == 5:
        print("Place your reservation soon! 5 minutes remaining.")
    elif mins == 2:
        print("Don't lose your seats! 2 minutes remaining.")
    elif mins == 0:
        print("User timed out.")
    else:
        print(mins)
    
    mins -= 1
    sleep(1)
