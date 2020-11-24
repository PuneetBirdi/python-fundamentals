# A for loop is used for iterating over a sequence, (that is either a list, a tuple, a dictionary or a string)
people = ['John', 'Will', 'Nancy', 'Karen']

# Simple for loop
for person in people:
    print('Current person: ', person)

# Break out a for loop
for person in people:
    if person == 'Will':
        break
    print('Current person: ', person)

# Continue
for person in people:
    if person == 'Will':
        continue
    print('Current person: ', person)

# Range, this range can be any numbers
for i in range(len(people)):
    print('Current Person: ', people[i])

for i in range(0, 10):
    print('Number: ', i)

# A while loop executes a set of statements as long as a condition is true.
count = 0
while count <= 10:
    print('Count: ', count)
    count += 1
