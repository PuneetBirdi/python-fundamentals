# Working with JSON in python.
import json

# Sample JSON
userJSON = '{"first_name":"Puneet", "last_name":"Birdi","age":24}'

# Parse to dict
user = json.loads(userJSON)

print(user)
print(user['first_name'])


car = {'make': 'ford', 'model': 'Mustang', 'year': 1970}

carJSON = json.dumps(car)
print(carJSON)
