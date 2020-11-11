"""
    Python has this module to work with abstract classes
    ABCMeta makes our class abstract
"""
from abc import ABCMeta, abstractmethod


class Movable(metaclass=ABCMeta):
    
    @abstractmethod
    def move(self):
        """Abstract method"""
    
    @property
    @abstractmethod
    def speed(self):
        pass


class Bus(Movable):

    speed = 10
    # or
    # def speed(self):
    #     return 10

    def go(self):
        print(f'Bus went at speed {self.speed}')
    
    def move(self):
        self.go()


bus = Bus()
bus.move()
