# Создать функцию fib для нахождения числа фибоначчи и закэшировать данные в файл
# (результаты записываются в файл если в файле есть уже ответ числа фибоначчи то не вычисляем а просто его берем). 
# В созданный файл записать результаты функции fib, если данные есть то не записываем а берем их и печатаем.
import csv


def cache_file(func):
    num_fibonacci = {}
    try:
        with open('fibonacci.csv', mode='r') as csv_file:
            reader = csv.reader(csv_file)
            for num_tuple in reader:
                num_fibonacci[int(num_tuple[0])] = int(num_tuple[1])
    except FileNotFoundError:
        print('File is not found, so we will create new one')
        open('fibonacci.csv', 'w').close()
    
    def inner_func(number: int):
        if number in num_fibonacci.keys():
            value_to_return = num_fibonacci[number]
        else:
            value_to_return = func(number)
            num_fibonacci[number] = value_to_return
            with open('fibonacci.csv', mode='w', newline='') as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                for num, fib in num_fibonacci.items():
                    writer.writerow([num, fib])

        return value_to_return

    return inner_func


@cache_file
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(100))
