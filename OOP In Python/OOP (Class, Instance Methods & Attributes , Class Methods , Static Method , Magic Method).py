
# python support object orianted programming
# OOP is a paradigm or coding style
# paradigm : Means structuring program so the Methods [functions] and attributes [Data] Are Bundled into objects
# ,ethods act as function that use the information of the object
# Python is Multi-Paradigm programiming language [Procedural , OOP , Functional ]
# procedural : structure App like recipe , sets of steps to make the task
# functional : Built on the concept of Mathematical Functions

# What is OOP?
# OOP allow you to organize your code and Make it readable and reusable
# Everything in python is object


# Class syntax and info
# [01] Class it the Blueprint of constructor of the object
# [02] Class instantiate Means create instance of a class
# [03] instance is object created from class and have their methods and attributes
# [04] class defined with keyword class
# [05] class name written with pascalcase [Uppercamelcase] style
# [06] class may contains Methods and attributes
# [07] When Creating Object Python Look For The Built In __init__ Method
# [08] __init__ Method Called Every Time You Create Object From Class
# [09] __init__ Method Is Initialize The Data For The Object
# [10] Any Method With Two Underscore in The Start and End Called Dunder or Magic Method
# [11] self Refer To The Current Instance Created From The Class And Must Be First Param
# [12] self Can Be Named Anything
# [13] In Python You Dont Need To Call new() Keyword To Create Object
# -------------------------------------------------------------------
# Syntax
# class Name:
#     Constructor => Do Instantiation [ Create Instance From A Class ]
#     Each Instance Is Separate Object
#     def __init__(self, other_data)
#         Body Of Function
class Member:
    def __init__(self):
        print("a new member has been added ")

# Create an instance of the Member class
member = Member() # a new member has been added


# Instance Attributes and Methods
# Self: Point To Instance Created From Class
# Instance Attributes: Instance Attributes Defined Inside The Constructor
# -----------------------------------------------------------------------
# Instance Methods: Take Self Parameter Which Point To Instance Created From Class
# Instance Methods Can Have More Than One Parameter Like Any Function
# Instance Methods Can Freely Access Attributes And Methods On The Same Object
# Instance Methods Can Access The Class Itself
# -----------------------------------------------------------

class Student:
    def __init__(self,first_name):
        self.name = first_name

s1 = Student("salma")
print(s1.name) # salma

# Instance Attributes and Methods
# Self: Point To Instance Created From Class
# Instance Attributes: Instance Attributes Defined Inside The Constructor
# -----------------------------------------------------------------------
# Instance Methods: Take Self Parameter Which Point To Instance Created From Class
# Instance Methods Can Have More Than One Parameter Like Any Function
# Instance Methods Can Freely Access Attributes And Methods On The Same Object
# Instance Methods Can Access The Class Itself
# -----------------------------------------------------------
class employee:
    def __init__(self,first_name,mid,last):
        self.name = first_name
        self.midname=mid
        self.lastname=last

    def full_name(self):
        print(f"your full name is {self.name} {self.midname} {self.lastname}")

s1 = employee("salma","mamdoh","sabry")
s1.full_name() # your full name is salma mamdoh sabry

# Class Attributes
# Class Attributes: Attributes Defined Outside The Constructor

"""
class Person:
    not_allowed_names=["hell","Bad","shit"]
    cnt=0;
    def __init__(self, first_name, middle_name, last_name, gender):
        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name
        self.gender = gender
        Person.cnt+=1

    def full_name(self):
        if self.fname  not in Person.not_allowed_names:
            return f"{self.fname} {self.mname} {self.lname}"
        else:
            return "This name is not allowed"

    def name_with_title(self):
        if self.gender == "Male":
            return f"Hello Mr {self.fname}"
        elif self.gender == "Female":
            return f"Hello Miss {self.fname}"
        else:
            return f"Hello {self.fname}"

    def get_all_info(self):
        return f"{self.name_with_title()}, Your Full Name Is: {self.full_name()}"
    def delete_user(self):
        Person.cnt-=1
        return f"user {self.fname} has been deleted"

p1=Person("hell","kk","oo","Male")
print(p1.full_name()) # This name is not allowed
print(Person.cnt) # 1
print(p1.delete_user()) # user hell has been deleted
print(Person.cnt) # 0
"""

# Class Methods & Static Methods
# Class Methods:
# - Marked With @classmethod Decorator To Flag It As Class Method
# - It Take Cls Parameter Not Self To Point To The Class not The Instance
# - It Doesn't Require Creation of a Class Instance
# - Used When You Want To Do Something With The Class Itself
# Static Methods:
# - It Takes No Parameters
# - Its Bound To The Class Not Instance
# - Used When Doing Something Doesnt Have Access To Object Or Class But Related To Class
# -----------------------------------------------------------
class Person:
    not_allowed_names=["hell","Bad","shit"]
    cnt=0;
    def __init__(self, first_name, middle_name, last_name, gender):
        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name
        self.gender = gender
        Person.cnt+=1

    def full_name(self):
        if self.fname  not in Person.not_allowed_names:
            return f"{self.fname} {self.mname} {self.lname}"
        else:
            return "This name is not allowed"

    def name_with_title(self):
        if self.gender == "Male":
            return f"Hello Mr {self.fname}"
        elif self.gender == "Female":
            return f"Hello Miss {self.fname}"
        else:
            return f"Hello {self.fname}"

    def get_all_info(self):
        return f"{self.name_with_title()}, Your Full Name Is: {self.full_name()}"
    def delete_user(self):
        Person.cnt-=1
        return f"user {self.fname} has been deleted"
    @classmethod
    def show_user_count(cls):
        print(f"we have {cls.cnt}  in out system")
    @staticmethod
    def say_hello():
        print("hello in our class with static method ")

p1=Person("salma","Mamdoh","Sabry","Female")
p1.show_user_count() # we have 1  in out system

p1.say_hello() # hello in our class with static method


# Magic Methods
# Everything in Python is An Object
# __init__  Called Automatically When Instantiating Class
# self.__class__ The class to which a class instance belongs
# __str__   Gives a Human-Readable Output of the Object
# __len__   Returns the Length of the Container
#           Called When We Use the Built-in len() Function on the Object
# ------------------------------------------------------

class skill:
    def __init__(self):
        self.skills = ["html", "css"]

    def __str__(self):
        return f"my skills are {', '.join(self.skills)}"
    def __len__(self):
        return len(self.skills)


prof = skill()
print(type(prof))  # <class '__main__.skill'>
print(prof)  # my skills are html, css
prof.skills.append("sql")
print(len(prof)) #3

