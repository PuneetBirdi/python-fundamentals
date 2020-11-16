'''
VARIABLE RULES:
 - Variable names are case sensitive
 - Must start with a letter or an underscore
 - Can have numbers but not start with one
'''

x = 1  # integer
y = 2.5  # float
name = 'Puneet'  # string
is_cool = True  # boolean

# Assigning multiple variables shorthand
x, y, name, is_cool = (2, 3.5, 'Not-Puneet', False)

print(x, y, name, is_cool)

# Basic math
a = x + y

print(a)

# Check type
print(type(x))

# Casting
x = str(x)
print(type(x))
