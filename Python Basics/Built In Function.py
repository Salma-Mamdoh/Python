# built in functions in pthon
# all()
# any()
# bin()
# id()
# sum()
# round()
# range()
# abs ()
# pow()
# min()
# max()
# slice()
# map()
# filter()
# Reduce()
# enumerate()
# help()
# reversed()


x=[1,2,3,5]
if all(i%2==0 for i in x):
    print("all is even numbers ")
else :
    print("Not all are even numbers  ")



if any(i%2==0 for i in x):
    print("any is even numbers ")
else :
    print("Not any even number exist ")


# bin return binary
print(bin(10)) # 0b1010

# id address of variable or object in memeory
print(id(x)) # 1748805939008

# sum ------> can take start os sum default sum is zero
print(sum(x)) # 11
print(sum(x,100)) # 111

# round (number , numofdigits)
print(round(150.05555,2)) # 150.06

# range (start , end , step) step is optional default is 1
for i in range(0,len(x) , 2):
    print(x[i])
# output 1
# 3


# print  , is sperator like " "
print("salma mamdoh")
print("salma","mamdoh")

print("salma",end="") # make end

# abs
print(abs(-5)) # 5
print(abs(-100.19)) # 100.19

# pow (base , expo , mod) mod is optional
print(pow(2,3)) # 8
print(pow(2,3,2)) # 0

# min(item , item , ...) min(iterator)
print(min(x)) # 1
print(min("a","b","x")) # a
# max opposite of min

# slice(start , end , step) step is optional
a=["a","b","c","d"]
print(a[1:]) # ['b', 'c', 'd']
print(a[slice(1,len(a)+1)]) # ['b', 'c', 'd']

# map()
# take an function + iterator
# map called map because it map the function on ervery element
# the function can be pre defined function or lambda function

# use map with predefined function
yy=[1,2,3,4,5]
def multiplybytwo(xx):
    return xx*2

for i in list(map(multiplybytwo,yy)):
    print(i)
# output 2
# 4
# 6
# 8
# 10

# use map with lambda function

for i in list(map(lambda number: (f"_ the number is {number}"), yy)):
    print(i)

# output is
# _ the number is 1
# _ the number is 2
# _ the number is 3
# _ the number is 4
# _ the number is 5


# filter take a function +iterator
# filter run a function on every element
# the function can be pre_Defined function or lambda function
# filter out all elements for which the function return true
# the function need to return boolean value

# filter with bre defined function
def checknumber(xx):
   return xx>10

newlist=[100,105,120,140,118,1,2,3,5]

resultlist=filter(checknumber,newlist)
for i in resultlist :
    print(i)

# output 100
# 105
# 120
# 140
# 118

# lambda function with filter function

resultnewlist=filter(lambda number:(number>10), newlist)
for oo in resultnewlist:
    print(oo)
# output 100
# 105
# 120
# 140
# 118


# Reduce takse a function + iterator
# reduce run a function on first and second element and giv result
# then run function in result and third element
# then runc function on the result and forth element
# till one element is left and this is the result of reduce
# the function can be pre defined function of lambda function


# reduce with re defined function
from functools import reduce
def funsum(x1,x2):
    return x1+x2

mynumbers=[2,5,0,1,3]

endresult=reduce(funsum,mynumbers)
print(endresult) # 11

# reduce with lambda function

endresultwithlambdafunction=reduce(lambda x1 , x2 : (x1+x2),mynumbers)
print(endresultwithlambdafunction) # 11


# enumerate(iterable , start) default of start =0

myskills=["c++","Python","HTML","CSS","Java","JS","SQL","C#"]

for skill in myskills :
    print(skill)

# output
# c++
# Python
# HTML
# CSS
# Java
# JS
# SQL
# C#

myskillcounter=enumerate(myskills,0)
print(type(myskillcounter)) # <class 'enumerate'>
for skill in myskillcounter:
    print(skill)

# output
# (0, 'c++')
# (1, 'Python')
# (2, 'HTML')
# (3, 'CSS')
# (4, 'Java')
# (5, 'JS')
# (6, 'SQL')
# (7, 'C#')


# help()  get properties of any built in function
#print(help(hash(tuple(myskills))))

# reversed (iterable)
myskills=reversed(myskills)
for i in myskills:
    print(i)

# output
# C#
# SQL
# JS
# Java
# CSS
# HTML
# Python
# c++