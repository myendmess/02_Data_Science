# Create a list of tuples, each representing the name, age, and position of a
# player on a basketball team.
team = [
    ('Marta', 20, 'center'),
    ('Ana', 22, 'point guard'),
    ('Gabi', 22, 'shooting guard'),
    ('Luz', 21, 'power forward'),
    ('Lorena', 19, 'small forward'),
    ]
# Add new players to the list.
team = [
    ('Marta', 20, 'center'),
    ('Ana', 22, 'point guard'),
    ('Gabi', 22, 'shooting guard'),
    ('Luz', 21, 'power forward'),
    ('Lorena', 19, 'small forward'),
    ('Sandra', 19, 'center'),
    ('Mari', 18, 'point guard'),
    ('Esme', 18, 'shooting guard'),
    ('Lin', 18, 'power forward'),
    ('Sol', 19, 'small forward'),
    ]
# Instantiate an empty dictionary.
new_team = {}

# Loop over the tuples in the list of players and unpack their values.
for name, age, position in team:
    if position in new_team:                    # If position already a key in new_team,
        new_team[position].append((name, age))  # append (name, age) tup to list at that value.
    else:
        new_team[position] = [(name, age)]      # If position not a key in new_team,
                                                # create a new key whose value is a list
                                                # containing (name, age) tup.
new_team

# Examine the value at the 'point guard' key.
new_team['point guard']

# You can access the a dictionary's keys by looping over them.
for x in new_team:
    print(x)
    
    # The keys() method returns the keys of a dictionary.
new_team.keys()

# The values() method returns all the values in a dictionary.
new_team.values()

# The items() method returns both the keys and the values.
for a, b in new_team.items():
    print(a, b)