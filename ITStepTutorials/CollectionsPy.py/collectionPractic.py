import random as rand


# arr = []
# n = 5
# for i in range(n):
#     arr.append([ rand.randint(0, i) for i in range(0, 10) ])

# print(arr)

# # 2
# sum_arr = 0
# for elem in arr:
#     sum_arr += sum(elem)

# 3
# snakeList = []
# n = 4
# minB = 1
# maxB = n
# for i in range(n):
#     if (i % 2 == 0):
#         snakeList.append([ i for i in range(minB, maxB + 1) ])
#     else:
#         snakeList.append([ i for i in range(maxB, minB - 1, -1) ])
#     minB = maxB + 1
#     maxB += n

# for el in snakeList:
#     print(el)

# 4
# def swap(a, b) -> tuple:
    # # tuple of (b, a) copies like (a, b)
    # a, b = b, a
    # return a, b # functions return only 1 value, so this is tuple

# first = 12
# second = 3
# print(first, second)
# print(swap(first, second))

# 5
# def get_tuple(start: int, end: int):
    # list1 = [ rand.randint(start, end) for el in range(start, end) ]
    # return tuple(list1)

# tup1 = get_tuple(0, 6)
# tup2 = get_tuple(-5, 0)
# tup3 = tup1 + tup2
# print(tup1, tup2, tup3)
# print('Count of zeros in tup3:', tup3.count(0))
