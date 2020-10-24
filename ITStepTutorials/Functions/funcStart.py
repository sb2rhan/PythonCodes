# def sayHello(name, age=18) -> None:
#     print(f'Hello, {name}, you are {age} y.o.')

# sayHello('Bread', 20)
# sayHello('Bera')


# receives many arguments (компоновка)
# def add_sum(a, *b):
#     # return a + b
#     print(a, b)
#     return a + sum(b)

# print(add_sum(3, 2, 3, 1, 8, 98))

# # (распаковка)
# arr = [3, 1, 2, 5]
# a, b, c, d = arr
# print(a, b, c, d)

# # like list.extend()
# # * makes tuple from list
# arr2 = [*arr, 54, 23]
# print(arr2)


# # ** makes dictionary from the rest of parameters
# # {'key': 'value'}
# def sayName(name, **args):
#     if args['email'] == 'smit@gmail.com':
#         print('Hi Smit! I recognise you!')
#     print(name, args)

# # if we are running this file then it returns true
# # if we use this file as module then it is false
# if __name__ == "__main__":
#     sayName(name='Smit', age='23', email='smit@gmail.com', password='ienc9wn32')


#           Beneficial functions

# listN = [3, 1, 4, 2]
# sortedL = sorted(listN)
# print(sortedL)
# listS = ['q', 'f', 'c', 'a']
# sorted(listS)
# print(list(zip(listN, listS)))


# words = ['some', '23', 'cmake']

# # Both are the same
# # 1st implementation
# arr = [ i.title() for i in words ]
# print(arr)
# # 2nd implementation
# mappedWords = list(map(str.title, words))
# print(mappedWords)


# # Filtering ('23' is ignored)
# print(list(filter(str.isalpha, words)))


# def factorial(number):
#     if (number <= 1):
#         return number
#     return number * factorial(number - 1)

# print(factorial(120))
