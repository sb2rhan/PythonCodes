class Singleton(object):
    """
    Singleton is a pattern which means that instance of this class will be only 1 object

    About __new__ and __init__:
        Use __new__ when you need to control the creation of a new instance (class method)
        Use __init__ when you need to control initialization of a new instance (instance method)
        __new__ is the first step of instance creation. It's called first, and is responsible for returning a new instance of your class.
        In contrast, __init__ doesn't return anything; it's only responsible for initializing the instance after it's been created.
        In general, you shouldn't need to override __new__ unless you're subclassing an immutable type like str, int, unicode or tuple.
    """
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


single1 = Singleton()
single2 = Singleton()

print(single1, single2)
print(id(single1), id(single2)) # same identificators
