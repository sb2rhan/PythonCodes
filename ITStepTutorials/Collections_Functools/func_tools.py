# Functools
# a module of high-level functions
# they are used to modify other low-level functions
# so they are decorators
import functools


# lru_cache for storing repetetive data
import requests

# # caches get_webpage function

# @functools.lru_cache(maxsize=24)
# def get_webpage(module):
#     webpage = f'https://docs.python.org/3/library/{ module }.html'

#     response = requests.get(webpage)

#     if response.status_code == 200:
#         return response.text
#     else:
#         return None

# modules = ['os', 'functools', 'collections', 'sys']
# for m in modules:
#     html_page = get_webpage(m)
#     if html_page:
#         print(m, 'is found')
#     else:
#         print(m, 'is not found')


# Another example of lru_cache
# without lru_cache it is gonna stuck at numbers like 100 or more

# @functools.lru_cache()
# def fibonacci(n):
#     if n < 2:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(100))


# Partial
# allows us to invoke functions by parts
# so we can give some parameters at the first invoke
# and the rest of parameters at the next call

# def getGreetingByName(name, age, last_char='!'):
#     return f'Hello, {name}{last_char} You are {age} y.o.'

# result = functools.partial(getGreetingByName, name='Jack')
# print(result) # stored declaration with name parameter only
# print(result(age=20)) # now we can print cuz we give it age


# Singledispatch
# needed to overload functions

# @functools.singledispatch
# def print_with_type(arg):
#     print('object: %s' % arg)

# # registered only for int variables
# @print_with_type.register(int)
# def print_int(arg):
#     print('int: %s' % arg)

# @print_with_type.register(str)
# def print_str(arg):
#     print('string: %s' % arg)

# print_with_type(3)
# print_with_type([3, 1, 'kdsf'])
# print_with_type('Hello')

# print(print_with_type.dispatch(int)) # to determine what function dispatches this type


@functools.singledispatch
def add(collection):
    return sum(collection)

@add.register
def add_list(list1: list):
    return sum(list1)

@add.register
def add_dic(dictionary: dict):
    return {sum(dictionary.keys()): sum(dictionary.values())}

@add.register
def add_tuple(tuple1: tuple):
    return sum(tuple1)

@add.register
def add_int(num: int):
    return sum(range(1, num + 1))

print('-' * 30, 'Test of add funcs', '-' * 30)
print(add_int(5))
print(add_list([3, 1, 4]))
print(add_dic({3: 21, 12: 92}))
print(add_tuple((3, 12, 3)))
