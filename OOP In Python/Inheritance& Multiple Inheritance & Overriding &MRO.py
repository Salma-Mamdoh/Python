# OOP
# inheritance
# Multiple inheritance
# Method overriding
# Method Resolution order

class food:
    def __init__(self,name):
        self.name=name
        print(f"{self.name} food is created from base class")

    def eat(self):
        print("eat method from base class ")

class Apple(food):
    def __init__(self, name):
        super().__init__(name)
        print(f" {self.name} is created from drived class")

    # override
    def eat(self):
        print("override from derived class ")


food_one = food("pizza")
food_two= Apple("Cola")
food_two.eat()

# output
# pizza food is created from base class
# Cola food is created from base class
#  Cola is created from drived class
# override from derived class


class Baseone:
    def __init__(self):
        print("we are in Baseone")

    def fun1(self):
        print("One")

class Basetwo:
    def __init__(self):
        print("we are in BaseTwo")
    def fun2(self):
        print("Two")

class Derived(Baseone,Basetwo):
    pass


var=Derived() # we are in Baseone if the are not init print statement in derived class

# mro method resolution order
print(Derived.mro()) # [<class '__main__.Derived'>, <class '__main__.Baseone'>, <class '__main__.Basetwo'>, <class 'object'>]

var.fun1() # One
var.fun2() # Two

print(var.fun1) # <bound method Baseone.fun1 of <__main__.Derived object at 0x000001E73C067C10>>
print(var.fun2) # <bound method Basetwo.fun2 of <__main__.Derived object at 0x000001E73C067C10>>


class base:
    pass

class derivedone(base):
    pass

class derivedtwo(derivedone):
    pass

# derivedtwo will inherit derivedone and base 
