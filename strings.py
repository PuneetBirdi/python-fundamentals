name = 'Puneet'
age = 24

# Concatenation
# ________________________________________
# Note: you cannot concatenate a string with an int, you'd have to cast it into a string
print('Hello ' + name + ' ' + str(age))

# String formatting
# _________________________________________
# Arguemnts by position allows you to use placeholders with curly brackets.
# The numbers in the placeholder allow for you to rearrange positions.
print('{1}, {2}, {0}'.format('a', 'b', 'c'))

# Arguments by name
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (only in 3.6+), is a faster way, bypasing .format similar to template strings.
print(f'My name is {name} and I am {age}')


# String Methods
# _________________________________________
s = 'hello wOrld'
# Capitalize first letter
print(s.capitalize())

# Capitalize all letters
print(s.upper())

# Lowercase all letters
print(s.lower())

# Swap case
print(s.swapcase())

# Get Length
print(len(s))

# Replace
print(s.replace('wOrld', 'everyone'))

# Count by character
sub = "l"
print(s.count(sub))

# Starts with - returns true/false
print(s.startswith('h'))

# Ends with - returns true/false
print(s.endswith('k'))

# Split into a list - splits words into list (Array)
print(s.split())

# Find position
print(s.find('r'))

# Is alphanumeric - returns true/false and spaces return false
print(s.isalnum())

# Is alphabetic - returns true/false and spaces return false
print(s.isalpha())

# Is numeric - returns true/false and spaces return false
print(s.isnumeric())
