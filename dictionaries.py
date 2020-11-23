# A dictionary is a collection which is unordered, changeable and indexed with no duplicate members. Note: very similar to a javascript object.

# Simple dict
person = {
    'first_name': 'Puneet',
    'last_name': 'Birdi',
    'age': 30
}

# Using a constructor
person = dict(
    first_name='Puneet',
    last_name='Birdi',
    age=30
)

# Access a single value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '123-456-7890'

# Get keys
print(person.keys())

# Get values
print(person.items())

# Make copy
person2 = person.copy()
person2['city'] = 'Mississauga'

# Remove item
del(person['age'])
person.pop('phone')

# Length
print(len(person2))

# List of dict
people = [
    {'name': 'Martha', 'age': 40},
    {'name': 'Snoop', 'age': 420}
]
print(people[1]['name'])

print(person)
