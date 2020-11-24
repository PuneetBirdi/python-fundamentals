# A module is a file containing a set of function to include in your application. There are core python modules, modules you can install using the pip package manager, and custom modules.

# Core Modules
# Import an entire module
import camelcase
import datetime
from time import time
# import just one thing from a module
from datetime import date


today = date.today()
print(today)

timestamp = time()
print(timestamp)


# Pip modules

camel = camelcase.CamelCase()
text = 'hello there friend'
print(camel.hump(text))



