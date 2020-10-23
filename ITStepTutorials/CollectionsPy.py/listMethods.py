arr = [ i for i in range(12, 0, -1) ]

# print(arr)

# arr.append(10)
# print(arr)

# # like append, but at index
# arr.insert(5, True)
# print(arr)

# # extend list
# listArr = [12, 22, 'Cmon']
# arr.extend(listArr)
# print(arr)

# # Remove methods
# arr.remove('Cmon')
# print(arr)

# deleted = arr.pop(5)
# print('Deleted element -', deleted)
# print(arr)

# del arr[3]
# print(arr)

# # count of this element
# elem = 3
# print(arr.count(elem))

# # length of array
# print(len(arr))

# # returns index of the element
# print(arr.index(5))

# # sorting void method
# # arr.sort(reverse=True) # descending
# arr.sort() # ascending
# print(arr)

# # Reverse methods
# arr.reverse()
# print(arr)

# print(arr[::-1])


    # Copy of list
# Naive copy work
brr = arr
brr[1] = 'Check'
print(id(arr), id(brr))
print(brr, arr)

# Proper Way
brr = arr.copy()
brr[1] = 'Check'
print(id(brr), id(arr))
print(arr)
print(brr)

# Or
brr2 = arr[:]
brr2[1] = 'Check'
print(id(brr2), id(arr))
print(arr)
print(brr2)

# Copying two-dimensional
arr = [[3, 2, 3], 20, [32, 33, 22]]
# brr = arr.copy()
# brr[0][1] = 'Hello' # will be same at two independent matrices
# print(brr, arr) # cause: inner lists are copied like assigning

# To solve that
from copy import deepcopy
brr = deepcopy(arr)
brr[0][1] = 'Hello'
print(brr, arr)