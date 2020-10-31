# 1) Даны целые положительные числа A и B (A < B). Вывести все целые
# числа от A до B включительно; при этом каждое число должно выводиться столько раз,
# каково его значение (например, число 3 выводится 3 раза).
a = 3
b = 17
for i in range(a, b + 1):
    print(str(i) * i)
print()

# 2) Описать функцию getSize(), которая находит размер бумаги по стандартному 
# формату.  А0, А1, А2, А3, А4, …. (https://ru.wikipedia.org/wiki/ISO_216)
import math


def recursiveSizeGet(width: float, length: float, type: int):
    if (type == 0):
        return width, length
    return recursiveSizeGet(length / 2, width, type - 1)

def getSize(type: int) -> tuple:
    width = round(1000 * (1 / math.sqrt(math.sqrt(2))), 0)
    length = round(1000 * math.sqrt(math.sqrt(2)), 0)

    if type < 0:
        return IndexError('Type must be greater than 0')
    
    return recursiveSizeGet(width, length, type)

    # by loop
    # while type > 0:
    #     length_save = length
    #     length = width
    #     width = length_save / 2
    #     type -= 1
    # return (width, length)

typeA4 = 4 # A4
print(f'Size of A{typeA4} paper is - {getSize(typeA4)}')
print()

# 3) Создать массив из 10 случайных чисел.
import random


random_list = [ random.randint(1, num + 10) for num in range(10) ]
print('Random created list:', random_list)
print()

# 4) Написать функцию, принимающую в качестве аргумента массив и возвращающая 
# с этого массива только четные числа. Вывести на экран результат работы 
# этой функции с массивом из задачи 3.
def get_evens_from_list(given_list: list) -> list:
    even_list = [ num for num in given_list if num % 2 == 0 ]
    return even_list

print('Even list:', get_evens_from_list(random_list))
print()

# 5) Написать функцию, принимающую в качестве аргумента целое число и возвращающая 
# массив чисел, на которые это число делится без остатка. Вывести результат 
# на экран со случайным числом.
def get_factorials(number: int) -> list:
    is_even = (number % 2 == 0)
    if is_even:
        factorials = [ num for num in range(1, number + 1) if number % num == 0 ]
    else:
        factorials = [ num for num in range(1, number + 1) if number % num == 0 ]
    
    return factorials

test = 10
print(f'Factorials of { test } are:', get_factorials(test))
print()

# 6) Создать массив из 10 элементов, каждый из которых будет представлять 
# из себя массив с числами на которые делится соответствующее число из массива 3. 
# (К примеру если массив имеет следующую структуру [8, 21, 6, 2, 6, 7, 9, 2, 1, 10], 
# то первый элемент в массиве будет массивом, состоящим из элементов 
# [1, 2, 4, 8], второй [1, 3, 7, 21] и т.д.)
factorials_list = [ get_factorials(num) for num in random_list ]

print('Factorials list:', factorials_list)
