import csv


with open('csv_write.csv', 'w', encoding='utf-8') as csv_f:
    filewriter = csv.writer(csv_f, delimiter=',')
    filewriter.writerow(['Имя', 'Class'])
    filewriter.writerow(['Айбек', '11'])
