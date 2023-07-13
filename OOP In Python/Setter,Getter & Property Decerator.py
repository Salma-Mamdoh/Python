# OOP
# Getter & Setter
class Member:
    def __init__(self,name):
        self.__name=name

    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name=name



one=Member("salma")
print(one.get_name()) # salma
one.set_name("POE")
print(one.get_name()) # POE


# Probery Decorator
# if you have method has one parameter which is self and only return value like age_in_dayes you can deal with it as property by @property decerator
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say_hello(self):
        return f"Hallo {self.name}"
    @property
    def age_in_days(self):
        return self.age *365

p1=person("salma",20)
print(p1.say_hello()) # Hallo salma
print(p1.age_in_days) # 7300
