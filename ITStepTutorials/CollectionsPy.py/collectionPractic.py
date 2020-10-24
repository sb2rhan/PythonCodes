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
snakeList = []
n = 4
minB = 1
maxB = n
for i in range(n):
    if (i % 2 == 0):
        snakeList.append([ i for i in range(minB, maxB + 1) ])
    else:
        snakeList.append([ i for i in range(maxB, minB - 1, -1) ])
    minB = maxB + 1
    maxB += n

for el in snakeList:
    print(el)
