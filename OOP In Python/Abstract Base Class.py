# OOP
# Abstract Base class
# - Class Called Abstract Class If it Has One or More Abstract Methods
# - abc module in Python Provides Infrastructure for Defining Custom Abstract Base Classes.
# - By Adding @absttractmethod Decorator on The Methods
# - ABCMeta Class Is a Metaclass Used For Defining Abstract Base Class
# --------------------------------------------------------------------
from abc import ABCMeta,abstractmethod

class Programming(metaclass=ABCMeta): # Abstract class
    @abstractmethod
    def has_oop(self):
        pass

class python(Programming):
    def has_oop(self):
        return "Yes"


class Bascal(Programming):
    def has_oop(self):
        return "NO"

#one=Programming() # # ypeError: Can't instantiate abstract class Programming with abstract method has_oop
two=python()
print(two.has_oop()) # Yes


