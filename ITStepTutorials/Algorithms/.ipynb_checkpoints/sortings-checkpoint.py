# Bubble sorting algorithm O(n*n)
def bubblesort(array: list):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j+1] = array[j+1], array[j]

test_list = [3, 232, 39, 31, 9, 12]
print('Before sort:', test_list)
bubblesort(test_list)
print('After sort:', test_list)


# Merge sorting algorithm O(n * log(n))
def mergesort(array: list):
    n = len(array)
    if (n == 1):
        return array
    middle_index = int(n / 2)
    left_half = array[:middle_index]
    right_half = array[middle_index:]
    mergesort(left_half)
    mergesort(right_half)

    i = 0
    j = 0
    k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            array[k] = left_half[i]
            i += 1
        else:
            array[k] = right_half[j]
            j += 1
        k += 1
    
    while i < len(left_half):
        array[k] = left_half[i]
        i += 1
        k += 1
    
    while j < len(right_half):
        array[k] = right_half[j]
        j += 1
        k += 1

test_list2 = [33, 91, 12, 31, 3, 98, 12, 34, 11, 9]
print('Before merge sort:', test_list2)
mergesort(test_list2)
print('After merge sort:', test_list2)


# Shell sorting algorithm 
def shellsort(array: list):
    inc = len(array)
    while inc:
        for i, el in enumerate(array):
            while i >= inc and array[i - inc] > el:
                array[i] = array[i - inc]
                i -= inc
            array[i] = el
        # special formula
        inc = 1 if inc == 2 else int(inc * 5 / 11)

test_list3 = [43, 10, 23, 23, 11, 90, 4]
print('Before shell sort:', test_list3)
mergesort(test_list3)
print('After shell sort:', test_list3)
