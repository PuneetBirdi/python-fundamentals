# A class is like a blueprint for creating object. An object has properties and methods(functions) associated with it. Almost everything in python is an object.


# Create class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}.'

    def has_birthday(self):
        self.age += 1

# Extend a class

class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and I owe a balance of {self.balance} dollars.'


# Intialize user object
puneet = User('Puneet B', 'email@email.com', 24)
nancy = User('Nancy B', 'email@email.com', 65)
jack = Customer('Jack W', 'email@email.com', 12)
# Edit property
nancy.age = 67
# Call method
nancy.has_birthday()
jack.set_balance(35000)
jack.has_birthday()
print(jack.balance)
print(jack.greeting())
print(puneet.greeting())
print(nancy.age)
