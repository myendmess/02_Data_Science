# The set() function converts a list to a set.
x = set(['foo', 'bar', 'baz', 'foo'])
print(x)

# The set() function converts a tuple to a set.
x = set(('foo','bar','baz', 'foo'))
print(x)

# The set() function converts a string to a set.
x = set('foo')
print(x)

# You can use braces to instantiate a set
x = {'foo'}
print(type(x))

# But empty braces are reserved for dictionaries.
y = {}
print(type(y))

# Instantiating a set with braces treats the contents as literals.
x = {'foo'}
print(x)

# The intersection() method (&) returns common elements between two sets.
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}
print(set1.intersection(set2))
print(set1 & set2)

# The union() method (|) returns all the elements from two sets, each represented once.
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
print(x1.union(x2))
print(x1 | x2)

# The difference() method (-) returns the elements in set1 that aren't in set2
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}
print(set1.difference(set2))
print(set1 - set2)

# ... and the elements in set2 that aren't in set1.
print(set2.difference(set1))
print(set2 - set1)

# The symmetric_difference() method (^) returns all the values from each set that
# are not in both sets.
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}
set2.symmetric_difference(set1)
set2 ^ set1