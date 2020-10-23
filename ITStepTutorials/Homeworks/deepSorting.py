#  Написать функцию которая будет сортировать все элементы список(вложенный список)
#  Рекурсия
#  Встроенные функций sort()
#  Проверка на тип isinstance(x, type)

def deeply_sort(alist: list) -> None:
    # converting list and str to tuples
    # we sort str and list by their length
    for i in range(0, len(alist)):
        if isinstance(alist[i], list):
            deeply_sort(alist[i])
            alist[i] = (len(alist[i]), alist[i])
        elif isinstance(alist[i], str):
            alist[i] = (len(alist[i]), alist[i])
    
    # manual sorting
    for i in range(1, len(alist)):
        curr = alist[i]
        pos = i - 1

        while (pos >= 0 and (alist[pos][0] if isinstance(alist[pos], tuple) 
                else alist[pos])) > (curr[0] if isinstance(curr, tuple) else curr):
            alist[pos + 1] = alist[pos]
            pos -= 1
        
        alist[pos + 1] = curr

    # Checking tuples and converting them back
    for kv in enumerate(alist):
        if isinstance(kv[1], tuple):
            alist[kv[0]] = kv[1][1]
    
    


test_list = [[2, 3, 1], 0, 9, 1, 12, ['Hello', 2, 4]]
deeply_sort(test_list)
print(test_list)
