from random import randint


test_arr = [3, 0, 12, 39, 12, 43, 93, 13, 35, 52, 11, 68]

# linear search algorithm O(n)
def linearsearch(value, array: list):
    # for i, elem in enumerate(array):
    #     if elem == value:
    #         return i
    # return None
    # or
    return array.index(value) if value in array else None

item = 35
print(f'{item} is in test_arr at index:', linearsearch(item, test_arr))

# Binary search algorithm O(log(n))
# for sorted arrays only 
arr = []
for i in range(9):
    arr.append(randint(10, 100)) 

arr.sort() 

print(arr)

item = int(input('Search item: '))

def binary_search(arr, item):
    mid = len(arr) // 2
    left = 0
    right = len(arr) - 1

    while arr[mid] != item and left <= right:
        if item > arr[mid]:
            left = mid + 1
        else: 
            right = mid - 1
        mid = (left + right) // 2

    if left > right: 
        return 'Element not found'
    else: 
        return mid

print(binary_search(arr, item))
