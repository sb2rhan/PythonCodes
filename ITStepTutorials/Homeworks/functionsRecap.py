# 1)  Создать массив из 5 случайных чисел.
import random as rand
import math


print('-' * 30)
randomArray = [rand.randint(0, a + 1) for a in range(5)]
print(randomArray)


# 2)  Посчитать сумму всех чисел из массива задачи 1.
sum = 0
for num in randomArray:
    sum += num
print(f'Sum of numbers in the list - { sum }')


# 3)  Написать функцию принимающую на вход массив и возвращающую сумму всех чисел этого массива.
def getSumOfList(arr: list) -> int:
    sum = 0
    for num in arr:
        sum += num
    return sum

print(f'Sum of number in the list by function - { getSumOfList(randomArray) }')


# 4)  Найти максимальное число из массива задачи 1.
maxNum = randomArray[0]
for num in randomArray:
    if num > maxNum:
        maxNum = num
print(f'Max num from the list is - { maxNum }')


# 5)  Написать функцию, которая принимает на вход массив и возвращает максимальное число из этого массива.
def getMaxOfList(arr: list) -> int:
    maxNum = arr[0]
    for num in arr:
        if num > maxNum:
            maxNum = num
    return maxNum

print(f'Max num from the list by function is - { getMaxOfList(randomArray) }')


# 6)  Найти минимальное число из массива задачи 1.
minNum = randomArray[0]
for num in randomArray:
    if num < minNum:
        minNum = num
print(f'Min num from the list is - { minNum }')


# 7)  Написать функцию, принимающую на вход массив и возвращающая минимальное число из этого массива. 
def getMinOfList(arr: list) -> int:
    minNum = arr[0]
    for num in arr:
        if num < minNum:
            minNum = num
    return minNum

print(f'Min num from the list by function is - { getMinOfList(randomArray) }')


# 8)  Создать массив из 10 случайных чисел.
print('-' * 30)
randomList = [rand.randint(0, a + 1) for a in range(10)]
print(f'randomList is - { randomList }')


# 9)  Написать функцию, принимающую в качестве аргумента массив и возвращающая с 
# этого массива только четные числа. Вывести на экран результат работы этой функции с массивом из задачи 8.
def getOnlyEvenNumbersFromList(arr: list) -> list:
    even_list = []
    for num in arr:
        if (num % 2 == 0):
            even_list.append(num)
    return even_list

print(f'Even numbers of randomList are - { getOnlyEvenNumbersFromList(randomList) }')


# 10)  Написать функцию, принимающую в качестве аргумента целое число и возвращающая массив чисел, 
# на которые это число делится без остатка. Вывести результат на экран со случайным числом.
def getListOfFactors(number: int) -> list:
    dividers = []
    if number % 2 == 0:
        for num in range(1, number):
            if number % num == 0:
                dividers.append(num)
    else:
        for num in range(1, number, 2):
            if number % num == 0:
                dividers.append(num)
    dividers.append(number)
    return dividers

chosen_num = 2048
print('List of factors of {} is - {}'.format(chosen_num, getListOfFactors(chosen_num)))


# 11)  Создать массив из 10 элементов, каждый из которых будет представлять из себя массив с 
# числами на которые делится соответствующее число из массива 8. (К примеру если массив имеет 
# следующую структуру [8, 21, 6, 2, 6, 7, 9, 2, 1, 10], то первый элемент в массиве будет 
# массивом, состоящим из элементов [1, 2, 4, 8], второй [1, 3, 7, 21] и т.д.)
list_of_factors = [ getListOfFactors(num) for num in randomList ]
print(list_of_factors)


# 12)  Описать функцию isEven(A) логического типа, возвращающую TRUE ,
# если целый параметр A является четным, и FALSE в противном случае.
print('-' * 30)
def isEven(A: int) -> bool:
    if A % 2 == 0:
        return True
    return False

print('5 is even:', isEven(5))
print('10 is even:', isEven(10))


# 13)  Даны два случайных набора целых чисел (может быть, с повторениями). Выдать без повторений
# в порядке возрастания все те числа, которые встречаются в обоих наборах. Решить задачу при помощи процедур.
print('-' * 30)
def getCommonNumbers(list1: list, list2: list) -> list:
    '''
        Creates two sets of two lists without duplicates,
        then finds the common numbers and sorts them
    '''
    set1 = []
    [ set1.append(val) for val in list1 if val not in set1 ]
    set2 = []
    [ set2.append(val) for val in list2 if val not in set2 ]

    commons = [ val for val in set1 if val in set2 ]
    commons.sort()
    return commons

first_list = [ rand.randint(0, a + 1) for a in range(1, 15) ]
second_list = [ rand.randint(0, a + 1) for a in range(1, 15) ]
print(f'first_list: { first_list }\nsecond_list: { second_list }')

commons = getCommonNumbers(first_list, second_list)
print(f'Common numbers are - { commons }')


# 14)  Написать функцию проверяющую строку на палиндром.
def checkIsPalindrome(string: str) -> bool:
    if string[:] == string[::-1]:
        return True
    return False

print('Tenet is palindrome: ', checkIsPalindrome('tenet'))
print('Text is palindrome: ', checkIsPalindrome('text'))
print('Malayalam is palindrome: ', checkIsPalindrome('malayalam'))


# 15)  Дана строка состоящая из слов разделенных пробелами, найти количество слов и собрать массив из слов.
test_str = 'text car builder seek exhaust'
list_str = test_str.split()
print('Count of words:', len(list_str))
print('Words:', list_str)


# 16)  Описать функцию getSize(), которая находит размер бумаги по стандартному формату. 
# А0, А1, А2, А3, А4, …. (https://ru.wikipedia.org/wiki/ISO_216)
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

typeA4 = 7 # A4
print(f'Size of A{typeA4} paper is - {getSize(typeA4)}')
