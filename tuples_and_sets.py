# A tuple is a collection which is orgered and unchangeable. It allows duplicate members.

# Simple tuple
fruit_tuple = ('Apple', 'Orange', 'Mango')
# Using a constructor
fruit_tuple_constructor = tuple(('Apple', 'Orange', 'Mango'))

# Get a single value
print(fruit_tuple[1])

# Cannot change values
# fruit_tuple[1] = 'Grape'

# Tuples with one value should have a trailing comma, otherwise it will just return the value as a string/int etc..
fruit_tuple_2 = ('Apple',)

# Get length of a tuple
print(len(fruit_tuple))

# You cannot delete single values of a tuple but you can delete the entire tuple
del fruit_tuple_2


# A Set which is a collection, unordered and unindexed. No duplicate members.
# Create a set using curly braces.
fruit_set = {'Apple', 'Orange', 'Mango', 'Apple'}

# Check if in set
print('Apple' in fruit_set)

# Add to a set
fruit_set.add('Grape')

# Remove fromt set
fruit_set.remove('Mango')

# Clear set
fruit_set.clear()

# Delete set
del fruit_set

print(fruit_set)
