# Open a file
myFile = open('myFile.txt', 'w')

# Get Info
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I love Python')
myFile.write(' and JS.')
myFile.close()

# Append to file
myFile = open('myFile.txt', 'a')
myFile.write(' I also like SQL.')
myFile.close()

# Read from file - takes the first x characters of the file.
myFile = open('myFile.txt', 'r+')
text = myFile.read(10)
print(text)
