#       Creation of tuples
# tuples are not mutable

# a = (10, 2, 1.3, 'stack', True)
# print(a)
# print(type(a)) # gives the class of element

# b = tuple([212, 'H', False, -3]) # another way of creating tuple
# print(b)

# Tuples are lighter than lists by size of bytes
# l = [1, 2, 4]
# t = (1, 2, 4)
# print('List size:', l.__sizeof__())
# print('Tuple size:', t.__sizeof__())


#       Some operations

# tup1 = (32, 12, 9, 45, 'Rr', 5)
# tup1_sl = tup1[1:4]
# print(tup1)
# print(tup1_sl)

# del tup1[3] # will be TypeError cannot modify tuples
