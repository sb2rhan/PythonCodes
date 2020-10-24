def add_decorator(func):
    def modified_add(a, b):
        a **= 2
        b **= 2
        return func(a, b)
    return modified_add

"""
Decorators are used to affect results of function,
but not modify function or change it.
With them we can add some functinality to the function.
"""
@add_decorator
def add(a, b):
    return a + b

print(add(2, 4)) # will be 20 = 2^2 + 4^2
