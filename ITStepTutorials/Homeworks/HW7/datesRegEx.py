# 1. Сформировать массив из 10 случайных дат в формате ДД-ММ-ГГГГ. Далее при помощи 
# регулярных выражений преобразовать эти даты в формат ГГГГ.ДД.ММ
import datetime
from random import randrange
import re


start_date = datetime.date(1990, 1, 1)
end_date = datetime.date(2100, 1, 1)

days_range = (end_date - start_date).days

dates = []
for i in range(10):
    d = start_date + datetime.timedelta(days=randrange(days_range))
    dates.append(d.strftime('%d-%m-%Y'))
print(dates) # DD-MM-YYYY

for i in range(len(dates)):
    dates[i] = datetime.datetime.strptime(dates[i], '%d-%m-%Y').strftime('%Y.%d.%m')
print(dates) # YYYY.DD.MM
