#  Dictionary or maps in python

# Person = {}  # curly brackets are dictionary symbol
# Person["first"] = "Batyrkhan"  # [key] = value
# Person["last"] = "Sharipbay"

# Susan = {"first" : "Susan", "last" : "Ibach"}  # "key" :  "value"
# print(Person)
# print(Susan)


# List of dictionaries 
# Lists could store any types together, you could store there int, string, float together

# people = [Person, Susan]
# people.append({"first": "Bill", "last" : "Gates"})  # append means adding synonim
# people.append({"first": "John", "last" : "Harrison"})
# presenters = people[1: 3]    # presenters now is the list that contains people from 1st index to 2nd index(3rd is not included)
# print(presenters)            # prints the whole presenters list
# print(people)                # prints the whole people list
# print(len(people))           # length of the list



# from array import array     # library of array 
# # Unlike lists, arrays cannot store any types together

# numbers = array("d")  # d means digital, so this array stores only digital elements
# numbers.append(98)
# numbers.append(35)
# numbers.append(345)
# print(numbers)
# print(numbers[0]) #index