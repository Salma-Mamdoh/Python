# OOP
# Ploymorphism
class A:
    def do(self):
        print("From A")
        raise NotImplementedError("Derived classes must implement this method")

class B(A):
    # override
    def do(self):
        print("From B")

var=B()
var.do() # From B


# Encapsulation
# - Restrict Access To The Data Stored in Attirbutes and Methods
# Public
# - Every Attribute and Method That We Used So Far Is Public
# - Attributes and Methods Can Be Modified and Run From Everywhere
# - Inside Our Outside The Class
# Protected
# - Attributes and Methods Can Be Accessed From Within The Class And Sub Classes
# - Attributes and Methods Prefixed With One Underscore _
# Private
# - Attributes and Methods Can Be Accessed From Within The Class Or Object Only
# - Attributes Cannot Be Modified From Outside The Class
# - Attributes and Methods Prefixed With Two Underscores __
# ---------------------------------------------------------
# - Attributes = Variables = Properties
# -------------------------------------
"""
class Member:
    def __init__(self,name):
        self.name=name

one=Member("salma")
print(one.name) # salma ---> name is public
one.name="Roaa"
print(one.name) # Roaa
"""

""""
class Member:
    def __init__(self,name):
        self._name=name

one=Member("salma")
print(one.name) # error 
print(one._name) # salma
# Can not print it as name is protected attribute can be used in the class and derived class
# Note there are not a restriction this made to tell developers that this attribute is protectes
# if you write one._name is will print 

"""

class Member:
    def __init__(self,name):
        self.__name=name

    def say_hello(self):
        print(f"hallo {self.__name}")

one=Member("salma")
#print(one.name) # error
# print(one.__name) # error
# as name is a private attribute can access it only in its  class by methods in this class and inherited classes also
one.say_hello()# hallo salma

# there are way to print private attributes
print(one._Member__name) # salma


# at conclusion there are not restrictions in python for private and protected there are only keywords for developers to understand each other


