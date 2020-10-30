# 1. Записать в переменную случайное число и вывести на экран. (используйте функцию rand(0, 10000)).
from random import randint
import math
import re

print('1st task')
var = randint(0, 10000)
print(var)

# 2. Вывести на экран "even", если число из задачи 1 четное и вывести "odd", если - нет.
what_is_var = "even" if var % 2 == 0 else "odd"
print(what_is_var)

# 3. Найдите сумму всех чисел, на которое делится число из задачи 1.
print('3rd task')
sum = 0
if what_is_var == "even":
    for num in range(1, var + 1):
        if var % num == 0:
            sum += num
else:
    for num in range(1, var + 1, 2):
        if var % num == 0:
            sum += num

print('Sum of all numbers:', sum)

# 4. Найдите сумму всех четных чисел, на которые делится число из задачи 1.
print('4th task:')
sum = 0
if what_is_var == "even":
    for num in range(1, var + 1):
        if var % num == 0 and num % 2 == 0:
            sum += num

print('Sum of even numbers:', sum)
print()

# 5. Создать массив из 5 элементов, каждый из которых представляет из себя массив 
# из 10 случайных слов из любого текста, при этом каждое слово должно быть с заглавной буквы.
text = "Hello dear friend, world! How are you today? What's up! Glasses, restaurant, laptop, pen, drive - He needs them all."
all_words = re.findall(r"\b\w{2,}\b", text)
# print(all_words)
print('5th task:')
words_lists = []
for ls in range(5):
    ls = [ all_words[randint(0, len(all_words) - 1)].capitalize() for i in range(len(all_words)) ]
    words_lists.append(ls)

print(words_lists)
print()

# 6. Найдите сумму всех нечетных чисел, на которые делится число из задачи 1.
print('6th task:')
sum = 0
if what_is_var == "even":
    for num in range(1, var + 1):
        if var % num == 0 and num % 2 != 0:
            sum += num
else:
    for num in range(1, var + 1, 2):
        if var % num == 0 and num % 2 != 0:
            sum += num

print('Sum of odd numbers:', sum)
print()

# 7. Таблица умножения(a = input()).
print('7th task:')
num = int(input('Enter a number: '))

for a in range(1, 11):
    print(f'{num} * {a} = {num * a}')
print()

# 8. Нарисуйте 1-рис используя циклы (крестик)
print('8th task:')
for i in range(11):
    for j in range(11):
        if i == j or i + j == 10:
            print('X ', end='')
        else:
            print('- ', end='')
    print()
print()

# 9. Сформировать массив из 10 случайных строк (в каждой строке по  10 случайных символов [ABCD]), 
# далее при помощи регулярных выражений заменить в этих строках все повторяющиеся вхождения 
# на число повторений с соответствующим символом (Например AABCDDDBCC - 2ABC3DB2C).
print('9th task')
letters = 'ABCD'
strings = []
for i in range(10):
    s = ''
    for j in range(10):
        s += letters[randint(0, len(letters)-1)]
    strings.append(s)

print('Created list of strings:', strings)

for i, s in enumerate(strings):
    mod_str = ''
    for j in range(len(s)):
        if len(s) == 0:
            break
        found_group = re.search(f'{s[0]}+', s).group()

        len_found = len(found_group)
        if (len_found > 1):
            mod_str += str(len_found) + found_group[0]
        else:
            mod_str += found_group
        s = s[len_found:]

    strings[i] = mod_str

print('Modified list:', strings)
