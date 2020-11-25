# A function is a block of code which only runs when it is called. In python we do not use parentheses or curly brackets, we use indentation with tabs or spaces.

# Create function

# The equal in the arguement is a default value that would be overriden by any arguement that's passed through when the function is called.
def sayHello(name='buddy.'):
    """
    Prints hello and then name. This is a docstring that is meant to describe what the function does.
    """
    print('Hello ' + name)


# Return value
def getSum(num1, num2):
    total = num1 + num2
    return total


def getProd(num1, num2):
    total = num1 * num2
    return total


numSum = getSum(2, 3)


def addOnetoNum(num):
    num += 1
    return num


num = 5
new_num = addOnetoNum(num)
print(getProd(1, 5))
print(new_num)


# A lambda function is a small anonymous function.
# A lamba function can take any number of arguments. Very similar to JS arrow functions.
