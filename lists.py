# A list is a collection which is ordered and changeable. It allows duplicate members.
# A list is basically an array.

# Create a list
numbers = [1, 2, 3, 4, 5]

# Using a constructor
numbers = list((1, 2, 3, 4, 5, 6))
fruits = ['apples', 'oranges', 'grapes', 'pears']

# Get value by position
print(fruits[3])

# Get Length
print(len(fruits))

# Append to list
fruits.append('mangos')

# Remove from list
fruits.remove('grapes')

# Insert into position
fruits.insert(2, 'strawberries')

# Remove from position
fruits.pop(3)

# Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)
