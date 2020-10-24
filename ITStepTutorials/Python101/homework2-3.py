# By Sharipbay Batyrkhan


# 1.
# a = 3
# b = 90
# arrByIndex = enumerate(range(a, b + 1))
# for keyValue in arrByIndex:
#     print('arrByIndex[' + str(keyValue[0]) + '] =', keyValue[1])

# print('Count of all elements in arrByIndex is', keyValue[0] + 1)


# 2.
# a = 5
# b = 100
# arr = range(a, b + 1)

# for i in arr:
#     print(str(i) + '^2 =', i**2)


# 3.
# a = 7
# b = 20

# for kv in enumerate(range(a, b + 1)):
#     i = kv[0]
#     while i >= 0:
#         print(kv[1])
#         i -= 1


# 4.
# a = 5
# b = 15
# for i in range(a, b + 1):
#     j = i
#     while j > 0:
#         print(i)
#         j -= 1


# 5.
# a = 12
# b = 34
# for v in range(a, b + 1):
#     if v % 2 == 0:
#         print(v)


# 6.
# a = 3
# b = 20
# sum = 0
# for value in range(a, b + 1):
#     if not(value % 2 == 0):
#         sum += value

# print('Sum of odd numbers -', sum)


# 7.
# test_number = 392
# print('Number is -', test_number)

# number_str = str(test_number)
# sum = 0
# multipl = 1
# for i in number_str:
#     sum += int(i)
#     multipl *= int(i)

# print('Sum of its digits -', sum)
# print('Multiplication of its digits -', multipl)
# print('Inversed number is -', number_str[::-1])

# alt_str = list(number_str)
# alt_str[0], alt_str[1] = alt_str[1], alt_str[0]
# print('Changed ones and tens -', ''.join(alt_str))


# 8.
# array = []
# for value in range(15, 30):
#     array.append(randint(0, value))

# print(array)


# 9.
# list_test = list(range(0, 100, 17))
# print(list_test)


# 10.
# arrL = []
# for i in range(-20, 21):
#     arrL.append(i)

# countNeg = 0
# for i in arrL:
#     if i < 0:
#         countNeg += 1
# print("Count of negative numbers -", countNeg)

# arrWords = []
# countArr = []
# for i in range(5):
#     arrWords.append(input('Enter your word: '))

# for word in arrWords:
#     countArr.append(len(word))

# print('Words are:', arrWords)
# print('Count of each word:', countArr)
