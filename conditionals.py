# If/Else conditions are used to decide to do something based on something being true or false.

x = 1
y = 2


# Comparison operators (==, !=, >, <, >=, <= ) are used to compare values.

# Simple if
if x == y:
    print(f'{x} is equal to {y}')

# Simple if else
if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{x} is not greater than {y}')

# elif
if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{x} is not greater than {y}')

# Nested If
if x > 2:
    if x <= 10:
        print(f'{x} is greater than 2 and less than 10')

# Logical operators (and, or and not) - Used to combine conditional statements.

if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less than 10')

if x > 2 or x <= 10:
    print(f'{x} is greater than 2 or less than 10')

if not(x == y):
    print(f'{x} is not equal to {y}')

# Membership operators (not, not in) - Membership operators are used to test if a sequence is presented in an object.

numbers = [1, 2, 3, 4, 5]

# in
if x in numbers:
    print(f'{x} does exist in this array.')

# not in
if y not in numbers:
    print(f'{y} does not exist in this array.')

# Identity operators (is, is not) - Compare the objects, not if they are equal but if they are the same objects with the same memory allocation.

if x is y:
    print(x is y)

if x is not y:
    print(x is not y)
