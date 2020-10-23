"""
Every file is module in Python
you can import them anywhere
Modules are handy feature of Python
like namespaces.

To install additional modules(in terminal):
> pip install module_name
You can search modules in pypi website
"""

# from mainM.py file getting these methods
from mainM import sayHi, getFullName
# from mainM import * # or this

# testing the methods
sayHi('Baker')
print(getFullName('Bread', 'Winner'))
