# # 1
# print('2^179 =',2 ** 179)
# print('-' * 50, 'END', '-' * 50)
# print()

# # 2. Функция должна создать двумерный массив из случайного количества 
# # элементов и случайными числами(массив внутри массива)
# from random import randint


# def get_random_2dlist():
#     result_list = []
#     for i in range(randint(10, 30), randint(31, 50)):
#         list_1 = []
#         for j in range(i, randint(i + 1, 50)):
#             list_1.append(randint(-j // 2, j))
#         result_list.append(list_1)
#     return result_list

# random_list = get_random_2dlist()
# print('Random 2-dimensional list:', random_list)
# print('-' * 50, 'END', '-' * 50)
# print()

# # 3. Найти максимальный и минимальный элемент из списка ( список из 2 задачи)
# def get_minvalue_2d(list_2d: list):
#     mins = []
#     for list_1d in list_2d:
#         mins.append(min(list_1d))
#     return min(mins)

# def get_maxvalue_2d(list_2d: list):
#     maxs = []
#     for list_1d in list_2d:
#         maxs.append(max(list_1d))
#     return max(maxs)

# print('Min value of 2-dimensional list:', get_minvalue_2d(random_list))
# print('Max value of 2-dimensional list:', get_maxvalue_2d(random_list))
# print('-' * 50, 'END', '-' * 50)
# print()

# # 4. В отделе работают 3 сотрудника, которые получают заработную плату в рублях.
# # Требуется определить: на сколько зарплата самого высокооплачиваемого 
# # из них отличается от самого низкооплачиваемого. 100 500 1000 ~ 900
# employees = [
#     { 'first_name': 'Mark', 'last_name': 'Fred', 'salary': 34000 },
#     { 'first_name': 'Baron', 'last_name': 'Brad', 'salary': 400000 },
#     { 'first_name': 'John', 'last_name': 'Doe', 'salary': 50000}
# ]
# salaries = [ employee['salary'] for employee in employees ]
# print('Employees:', employees)
# print('Range of salaries:', max(salaries) - min(salaries))
# print('-' * 50, 'END', '-' * 50)
# print()

# # 5. Удалить Q элемент из списка
# def remove_element_2d(element, list2d: list):
#     for list1d in list2d:
#         if element in list1d:
#             list1d.remove(element)
    
# to_remove = random_list[5][0]
# print('Value to remove:', to_remove)
# print('Before remove:', random_list)
# remove_element_2d(to_remove, random_list)
# print('After remove:', random_list)
# print('-' * 50, 'END', '-' * 50)
# print()

# # 6. Отсортировать массив по возрастанию суммы цифр
# def sort_by_sum_of_list(list2d: list):
#     return sorted(list2d, key=sum)
        
# print('Before sort by sum:', random_list)
# random_list = sort_by_sum_of_list(random_list)
# print('After sort by sum:', random_list)
# print('-' * 50, 'END', '-' * 50)
# print()

# # 7. Напишите функцию, которая создаёт комбинацию двух списков таким образом:
# # [1, 2, 3] (+) [11, 22, 33] -> [1, 11, 2, 22, 3, 33]
# statement1 = input('Enter your first list:')
# statement2 = input('Enter your second list:')

# first_list = statement1.split(', ')
# second_list = statement2.split(', ')

# extended = []
# for i in range(len(first_list)):
#     extended.append(first_list[i])
#     if len(second_list) > i:
#         extended.append(second_list[i])

# for i in range(len(first_list), len(second_list)):
#     extended.append(second_list[i])

# print(f'{first_list} + {second_list} -> {extended}')
# print('-' * 50, 'END', '-' * 50)
# print()

# # 8. Посчитать количество одинаковых элементов в списке
# #    сделал через Counter
# from collections import Counter


# test_list = [3, 1, 33, 2, 0, 1, 3]
# print('We got this list:', test_list)
# elem_c = Counter(test_list)
# print('Identical elements in random list:', elem_c)
# print('-' * 50, 'END', '-' * 50)
# print()

# # 9. Дана строка. Заменить все символы 'a' и 'b' на 'A' и 'B' соответственно
# string = input('Enter any string(with letters a, b):')
# print('Before replace:', string)
# string = string.replace('a', 'A').replace('b', 'B')
# print('After replace:', string)
# print('-' * 50, 'END', '-' * 50)
# print()

# # 10. У вас есть массив чисел, составьте из них максимальное число. 
# # [9,3,1,6] = 9631
# def make_maxnum(list1: list) -> int:
#     str_list = [ str(elem) for elem in list1 ]
#     result = ''
#     while True:
#         if len(str_list) == 0:
#             break
#         max_num = max(str_list)
#         result = result + str(max_num)
#         str_list.remove(max_num)
#     return int(result)

# test_arr = [3, 1, 0, 9, 100]
# print('Given list:', test_arr)
# print('Max num from it:', make_maxnum(test_arr))
# print('-' * 50, 'END', '-' * 50)
# print()

# # 11. У вас есть массив чисел. Напишите функции которые вычисляют сумму этих чисел с рекурсией
# def recursion_sum(list1: list) -> int:
#     if len(list1) == 1:
#         return list1[0]
#     sum_num = list1[0]
#     return sum_num + recursion_sum(list1[1:])

# test_ls = [4, 1, 5, 6, 12]
# sumls = recursion_sum(test_ls)
# print(f'Sum of {test_ls} is {sumls}')
# print('-' * 50, 'END', '-' * 50)
# print()

# # 12. Преобразование времени: 07:05:45PM ~ 07:05:45 or 03:34:52AM ~ 15:34:52
# import re
# from datetime import datetime


# def converter_to_24hour(format12: str) -> str:
#     date12 = datetime.strptime(format12, '%I:%M:%S%p')
#     return date12.strftime('%H:%M:%S')

# def converter_to_12hour(format24: str) -> str:
#     date24 = datetime.strptime(format24, '%H:%M:%S')
#     return date24.strftime('%I:%M:%S%p')

# def time_format_changer(format: str) -> str:
#     pattern_12 = re.compile(r'\d{2}:\d{2}:\d{2}(AM|PM)')
#     pattern_24 = re.compile(r'\d{2}:\d{2}:\d{2}')

#     if pattern_12.match(format):
#         return converter_to_24hour(format)
#     elif pattern_24.match(format):
#         return converter_to_12hour(format)


# test_format1 = '12:00:12AM'
# print('First test:', test_format1, '~', time_format_changer(test_format1))
# test_format2 = '12:56:34'
# print('Second test:', test_format2, '~', time_format_changer(test_format2))
# print('-' * 50, 'END', '-' * 50)
# print()

# # 13. Функция линейного поиска в строке
# test_arr = [3, 0, 12, 39, 12, 43, 93, 13, 35, 52, 11, 68]

# def linearsearch(value, array: list):
#     return array.index(value) if value in array else None

# item = 35
# print(f'{item} is in test_arr at index:', linearsearch(item, test_arr))
# print('-' * 50, 'END', '-' * 50)
# print()

# # 14. Учитывая строку 0, N длины  который проиндексирован, напечатайте его символы с четным и 
# # нечетным индексами как строку разделенные пробелами, в одной строке Hacker ~ Hce akr
# def even_odd_letters(string: str) -> str:
#     evens = ''
#     odds = ''
#     for i, letter in enumerate(string):
#         if i % 2 == 0:
#             evens += letter
#         else:
#             odds += letter
#     return evens + ' ' + odds

# test_str = 'Hackerman'
# print(f'{test_str} is', even_odd_letters(test_str))
# print('-' * 50, 'END', '-' * 50)
# print()

# # 15. Дан список целых чисел. Заменить отрицательные на -1, положительные - на число 1, ноль оставить без изменений.
# def to_list_1to1(list1: list) -> list:
#     for i, elem in enumerate(list1):
#         if elem > 0:
#             list1[i] = 1
#         elif elem < 0:
#             list1[i] = -1

# t_list = [4, 1, 0, -4, 12, -3]
# print('Before:', t_list)
# to_list_1to1(t_list)
# print('After:', t_list)
# print('-' * 50, 'END', '-' * 50)
# print()

# # 16. 'MVEZ JEVU EPNPZ' расшифровать текст
# def decoder(encoded_str: str) -> str:
#     result = ''
#     for letter in encoded_str:
#         result += chr(ord(letter) - 1)
#     return result

# test_text = 'MVEZ JEVU EPNPZ'
# print('Decoded text:', decoder(test_text))
# print('-' * 50, 'END', '-' * 50)
# print()

# # 17. Найти значение списка, которое встречается чаще всего 
# # сделал через Counter
# test_list1 = [3, 4, 1, 'H', "c", 'H']
# identicals = Counter(test_list1)
# freq_key = identicals.most_common(1)[0]

# print('List:', test_list1)
# print('The most frequent element:', freq_key[0])
# print('-' * 50, 'END', '-' * 50)
# print()

# # 18. Написать функию которая находить сумму квадратов сделал через partial
# from functools import partial


# def sum_of_squares(a: int, b: int) -> int:
#     return a ** 2 + b ** 2

# part = partial(sum_of_squares, a=4)
# print('4^2 + 5^2 =', part(b=5))
# print('-' * 50, 'END', '-' * 50)
# print()

# # 19. Решить 18 задачу с помощью декоратора
# def square_values(function):
#     def inner_func(a: int, b: int):
#         a **= 2
#         b **= 2
#         return function(a, b)
#     return inner_func

# @square_values
# def sum_of(a, b):
#     return a + b

# print('4^2 + 5^2 =', sum_of(4, 5))
# print('-' * 50, 'END', '-' * 50)
# print()

# # 20. Использовать декоратор lru_cache для кэширование функции(основная функция ускорение процесса извлечения данных ).
# from functools import lru_cache

# @lru_cache(maxsize=24)
# def power(a, b):
#     return a ** b

# print('3^3000 =', power(3, 3000))
# print('4^12 =', power(4, 12))
# print('3^3000 =', power(3, 3000))
# print('-' * 50, 'END', '-' * 50)
# print()

# # 21. Написать программу которая сохраняет данные в словарь(данные берутся из бд)
# import mysql.connector

# config_db = {
#     'host': 'localhost',
#     'database': 'test_db',
#     'user': 'root',
#     'password': ''
# }

# try:
#     configs = config_db
#     db = mysql.connector.connect(**configs)

#     mc = db.cursor()
#     mc.execute('SELECT * FROM restaurants')
#     data = mc.fetchall()
#     data_dict = []
#     for tup in data:
#         data_dict.append({
#             'title': tup[1],
#             'link': tup[2],
#             'category': tup[3],
#             'rating': tup[4],
#             'extras': tup[5]
#         })
#     print(data_dict)

# except Exception as e:
#     print(e)
# finally:
#     if db.is_connected():
#         db.close()
