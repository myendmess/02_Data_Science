# This function takes an integer as an input and returns its factorial.
def factorial(n):
    # Exclude 0 as product, start with 1
    y = 1
    for i in range(int(n)):
        y = y*(i+1)
    return y

# Enter a numerical value between 1-9 in the command line that appears.
input_num = input("insert a number: ")
# Apply factorial function to an integer input
print(factorial(input_num))