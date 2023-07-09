# ---- iterable vs iterator ----

# iterable
# object contains data can be iteraded upon
# examples ( string , kist , set , tuple , dict)

# iterator
# object used to iterate over iterable using next() method return 1 element at a time
# You Can generate iterator from iterable when using iter() Method
# For loop Already calls iter() Method on iterator behind the scene
# gives "stopiteration" if there no next element



# Generators
# ---------------
# Generator is a function with "yield" keyword instead of "return"
# it support iteration and return generator oterator by calling "yield"
# generator function can have one or more "yield"
# by using next() it resume form where it called "yield" not from begining
# when called , its not start automatically , its only give you the control


def mygenerator():
    yield 1
    print(" i am here ")
    yield 2
    yield 3

print(mygenerator()) # <generator object mygenerator at 0x00000282D6D45D90>

mygen=mygenerator()

print(next(mygen))
# 1
#  i am here
print(next(mygen)) # 2
print(next(mygen)) # 3


for num in mygenerator():
    print(num)

# output
# 1
#  i am here
# 2
# 3


# decorators
# sometimes called meta programming
# everything in python object even functions
# decorator take a function and add some functionality and return it
# decrator wrap other function and enhance thier behaviour
# decrator is higher order function ( function accept function as a parameter )

def myDecorator(func):
    def nestedfunc():
        print("Before")

        func()

        print("after")
    return nestedfunc()

@myDecorator
def sayhello():
    print("halllooooooooooo")

sayhello
# output
# Before
# halllooooooooooo
# after

# instead of this way use @ myDecerator before sayhello function
# afterDecoration=myDecorator(sayhello)
# afterDecoration

# output
# Before
# halllooooooooooo
# after

# decorater with function with paremeters
def myDecorator2(func):
    def nestedfunc2(num1,num2):
        print("Before calculation ")

        func(num1,num2)

        print("after calculation" )
    return nestedfunc2
@myDecorator2  # note can do more than one decerator
def calc(a,b):
    print(a+b)

calc(5,10)

# output
# Before calculation
# 15
# after calculation




# can pass any numeber of arguments to nested function in decorator

def myDecorator3(func):
    def nestedfunc3(*numbers):
        print("Before calculation ")
        for num in numbers:
            if num<0 :
                print("there are negitive numbers ")
        func(*numbers)

        print("after calculation" )
    return nestedfunc3
@myDecorator3  # note can do more than one decerator
def calc(a,b,c):
    print(a+b+c)

calc(10,-10,10)
# output
# Before calculation
# there are negitive numbers
# 10
# after calculation

# decerator practical speed test
from time import time
def speedtest(func):
    def wrapper():
        start=time()
        print(f"start time is {start}")
        func()
        end=time()
        print(f"end time is {end}")

    return wrapper
@speedtest
def bigloop():
    for num in range(0,20000):
        print(num)

bigloop() # start time is 1688863246.440786
 # numbers from 0 tp 20000
 # end time is 1688863246.764146


# practical loop on many iterators with zip()

# zip() return A zip object contains all objects
# zip() length is the length of lowest object

list1=[1,2,3,4,5]
list2=['a','b']
tuple=("M","F","F")
collect=zip(list1,list2,tuple)
for i in collect:
    print(i)

# output
# (1, 'a', 'M')
# (2, 'b', 'F')


# practical image Manipulation with pillow
from PIL import Image
myImage=Image.open(r"C:\Users\smmdw\OneDrive\Desktop\2 semester 2 year\WhatsApp Image 2023-07-03 at 00.41.08.jpg")
#myImage.show()

myBox=(0,0,800,800)
mynewimage=myImage.crop(myBox)
#mynewimage.show()

myconverted=myImage.convert("L")
#myconverted.show() # make image with gray scale


# Doc String & commenting vs Documenting
# documentation string for class , module or function
# can be accessed from the help and doc attributes
# made for understanding the functionaliti of the complex code
# theres one line and multiple line Doc strings

def hello():
    '''this function to say hallo'''
    print("kkkkkkkkk")
# documontations saved in doc and help attribute
print(hello.__doc__) # this function to say hallo


# install and use pylint

