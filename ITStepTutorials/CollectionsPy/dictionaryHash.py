#       Dictionary       #

#  also it is map, hashtable, associative array
#  able to store elements by any type of index
#  used curly braces to create {}

#  Creation:
# dict1 = { 'key': 'value' }
# print(type(dict1))
# dict2 = dict(key = 'value')
# print(type(dict2))
# dict3 = dict([('age', 23), ('name', 'venom')])
# print(dict3)
# dict4 = dict(zip(['name', 'age'], ['mark', 32]))
# print(dict4)

#  Manipulation
user = {
    'name': 'admin',
    'password': 'fne93cce',
    'email': 'admin32@gmail.com',
    'age': 20,
    'nicknames': ['admin223', 'kekeus32'],
    (1, 2): { 'key': 'value' }
}
# print(user)
# # Getting access
# print(user['password'])
# print(user['nicknames'][1])
# print(user[(1, 2)])
# print(user.get('name')) # if not exists then None
# print(user.get('naem', 'nothing')) # if not exists then default value
# print(user.setdefault('Name')) # if there is element returns else creates
# print(user)                    # with 2nd value which is not given, so None

# print(len(user))
# print(user.keys())
# print(user.values())
# print(user.items()) # (key, value)
# print('name' in user) # old method has_key()

# for i in user: # only keys
#     print(i)

# for k, v in user.items(): # also .values(), .keys()
#     print(k, '-', v)
