class Car:

    mark = 'Tesla'
    model = 'P100D'
    year = 2019

    def start(self):
        return f'Car {self.mark} {self.model} has been started'

    def stop(self):
        return f'Car {self.mark} {self.model} has been stopped'

    """
    Difference between static method and class method:
        1. Static method behaves as method that is not included in the class, so it behaves as module function
        2. Class method takes cls argument and uses it for working with class
    """
    @staticmethod
    def get_info():
        return f'{Car.mark} {Car.model} {Car.year}'

    @classmethod
    def get_class_info(cls):
        return f'{cls.mark} {cls.model} {cls.year}'


# car1 = Car()
# print('Type of car1:', type(car1))
# car2 = Car()
# print(car1.mark)
# print(car2.model)
# print(car1.start())
# print(car2.stop())
# print(Car.get_info())
# print(Car.get_class_info())


class Man:

    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def get_name(self):
        return self.name

    def __str__(self):
        return f'{Man.__name__}: {self.name} {self.lastname}'


# user = Man('Mark', 'Wand')
# print('Is id exists in user object:', hasattr(user, 'id'))
# print('Let\'s create it')
# setattr(user, 'id', 1) # id will be only in user objects
# print(user, user.id) # __str__ method + id
# print(dir(Man))
# print(dir(user))


# # Static constructer
# class Counter:
#     count = 0

#     @staticmethod
#     def __init__():
#         Counter.count += 1
#         print(Counter.count)

# print(Counter())
# print(Counter())


# # Another type of constructor
# class Vehicle:
    
#     def __new__(cls):
#         print('New vehicle object')
#         return super(Vehicle, cls).__new__(cls)

#     def __init__(self):
#         print('Initiate class')

#     def __del__(self):
#         print('Delete class')


# v1 = Vehicle() # __new__ method works first then only __init__ method is invoked
# # in the end, __del__ destructor works


"""
    Modificators in Python is just an agreement between programmers
    So we just differentiate fields by _
"""
class Transport:

    def __init__(self):
        self.mark = 'Toyoto'  # public
        self._model = 'Camry' # protected
        self.__price = 300000 # private


# transport1 = Transport()
# print(transport1._model)  # will print
# print(transport1.__price) # will be error, cuz Python renames this property


"""
    Inheritance
    Actually, every class in Python inherits from object class
    We can show by parentheses it like this:
    class Example():
        pass
"""
class Horse:
    is_horse = True

    def race(self):
        print('Running in the race')


class Donkey:
    is_donkey = True

    def push(self):
        print('Pushing the goods')


class Mule(Horse, Donkey):
    is_mule = True


mule = Mule()
print(mule.is_donkey)
print(mule.is_horse)
print(mule.is_mule)
mule.race()
mule.push()
