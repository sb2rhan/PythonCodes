#  Lists contains any types together

# theList = ["apple", "banana", "orange", "kiwi", "cherry"]         #  [] defines list
# print(theList)
# print(theList[2])                                                 #  printing 3rd(2nd index) item of list
# print(theList[-2])                                                #  printing 2nd item from back of the list

# theList.reverse()                                                 #  reverse just reverses the whole list(last element now is 1st and first element is last)

# print(theList)

# for x in theList:                                              #  gonna print every item of list
#     print(x)

# if "apple" in theList:                                         #  by 'in' keyword finding apple in theList
#     print("Yes apple in this list")
# else:
#     print("No, apple is not in this list")

# range = theList[2: 4]                                          # range is now the list that contains from 2nd index to 3rd index of theList(4th index not included)
# print(range)

#  Also

# print(theList[: 4])                                            #  it will print from the beginning to 3rd index(4th index is not included)
# print(theList[2:])                                             #  it will print from the 2nd index to the end
# print(theList[-3: -1])                                         #  it will print from the 3rd item from the back
                                                                 #  to the 2nd item from the back(1st item from the back not included)

# theList.append("strawberry")                                   #  adding strawberry
# theList.insert(2, "melon")                                     #  inserting the melon to the 3rd position(2nd index)
# print(theList)
# mylist = theList.copy()                                        # copying theList to mylist
# mylist = list(theList)                                         # another way to copy

# theList.remove("apple")                                        #  removing item from the list
# theList.pop()                                                  #  pop removes by index or last item if nothing in brackets
# del theList[0]                                                 #  del removes 0 index
# theList.clear()                                                # clears the whole list
# del theList                                                    #  removes the whole list



# All functions of list

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list