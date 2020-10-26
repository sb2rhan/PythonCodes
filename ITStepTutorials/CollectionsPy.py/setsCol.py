#       Creation        #
# in sets there are no duplicates
# uses the same curly braces as dictionaries

# a = {1, 2, 'treck', True, 'lama'}
# print(type(a), a)
# b = set([32, 2])
# print(type(b), b)
# print('Elements of a:')
# for item in a:
#     print('  > ' + str(item))

# print(32 in b) # Check if it's there
# print(32 not in a)


#       Some methods        #
# It adds automatically in any order

# languages = {'c++', 'c#', 'javascript', 'java', 'python'}
# print(languages)
# languages.add('ruby')
# print(languages)
# languages.add('c#') # will not add
# print(languages)

# # Deletion
# languages.discard('c#')
# languages.remove('ruby')
# print(languages)

# # Update (Extend)
# a = {4, 3}
# b = {4, 1, 43}
# a.update(b)
# print(a)

# # Union
# set1 = {2, 4, 1, 'h'}
# set2 = {4, 2, 'h', 44}
# set_uni = set1.union(set2)
# set_uni1 = set1 | set2 # syntax sugar
# print('Union:', set_uni1)
# # Intersect
# set_intersect = set1.intersection(set2)
# set_intersect1 = set1 & set2 # syntax sugar
# print('Intersect:', set_intersect1)
# # Difference shows the unique elements of one set
# set_diff1 = set1.difference(set2) # 1
# set_diff2 = set2.difference(set1) # 44
# print('Difference:', set_diff1, set_diff2)
# # Symmetrical shows the uniques of both
# set_sdiff = set1.symmetric_difference(set2)
# print('Symmetric difference:', set_sdiff)

# Comparison
# a = {4, 3, 2, 5} # parent
# b = {4, 2} # child, cuz it contains some elements of a

# print(a <= b) # a is not child of b
# print(a >= b) # a is parent of b
# print('a is subset of b:', a.issubset(b)) # same as a <= b
# print('a is parent of b:', a.issuperset(b)) # same as a >= b

# c = {22, 0}
# print('c and a are not joined:', c.isdisjoint(a))
# print('c and b are not joined:',c.isdisjoint(b))
