import os

# Ensure the folder exists
os.makedirs('Loops and strings', exist_ok=True)

# Step 1: Write a local text file
with open('Loops and strings/zen_of_python.txt', 'w') as f:
    f.write("""Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
""")

# Step 2: Read the file line by line
with open('Loops and strings/zen_of_python.txt') as f:
    for line in f:
        print(line, end='')  # end='' prevents double spacing
print("\nI'm done.")
