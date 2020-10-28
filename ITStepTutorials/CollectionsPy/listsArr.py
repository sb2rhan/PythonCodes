#       List         #

# arr = []
# arr2 = list()

# print(type(arr) == type(arr2))

# # arr works in the same way as arr2
# arr = [ a ** 2 for a in range(1, 11)]
# print(arr)
# # but arr works faster
# arr2 = []
# for b in range(1, 11):
#     arr2.append(b ** 2)
# print(arr2)

array = [ a for a in 'hello world' if a != 'h']
print(array)

# arr = [1, 2, 'hello', 3, 'c', True, ['Wolrd', 3]]

# print(arr[6][0])
# print(arr[::2])
