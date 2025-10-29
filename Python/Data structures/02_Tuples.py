# Create a list of tuples, each representing the name, age, and position of a
# player on a basketball team.
team = [('Marta', 20, 'center'),
        ('Ana', 22, 'point guard'),
        ('Gabi', 22, 'shooting guard'),
        ('Luz', 21, 'power forward'),
        ('Lorena', 19, 'small forward'),
        ]

# Use a for loop to loop over the list, unpack the tuple at each iteration, and
# print one of the values.
for name, age, position in team:
    print(name)

# This code produces the same result as the code in the cell above.
for player in team:
    print(player[0])