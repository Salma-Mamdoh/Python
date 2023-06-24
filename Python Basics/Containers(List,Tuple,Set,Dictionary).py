# containers
# List and its methods
# tuples and its methods
# set and its methods
# Dictionary and its methods

# 1----------> LIST []
# List items are enclosed in square brackets
# List are ordered , to use index to access item
# List items is mutable ----> ADD , DELETE , EDIT
# List items is not unique
# List can have different data types
from typing import Set, List

myList=["salma","Mamdoh",1,2.0]
print(myList[0]) # salma
print(myList[-1]) # Mamdoh
print(myList[1:3]) # ['Mamdoh', 1]  note return list

print(myList[::2]) # ['salma', 1] 2 steps every time

myList[0:2]=[]
print(myList)# [1, 2.0]
myList[0:2]=['A','B']
print(myList) # ['A', 'B']

# List Methods

# append
myList.append("c")
myList.append("poe")
print(myList) # ['A', 'B', 'c', 'poe']

myList2=["i","a" , "new","list",22]
myList.append(myList2)
print(myList) # ['A', 'B', 'c', 'poe', ['i', 'a', 'new', 'list', 22]]
print(myList[-1]) # ['i', 'a', 'new', 'list', 22]
print(myList[-1][2]) # new


# extend method
a=[1,2,3,4,2]
b=["i","p","o","e"]
a.extend(b)
print(a) # [1, 2, 3, 4, 2, 'i', 'p', 'o', 'e'] notice diierence between append and extend


# remove ---> delete only first element have the value passed to remove function
a.remove(2)
print(a) # [1, 3, 4, 2, 'i', 'p', 'o', 'e']

# sort work on only one data type in the list
ss=[5,7,2,1,3,800]
ss.sort()
print(ss) # [1, 2, 3, 5, 7, 800]
ss.sort(reverse=True)
print(ss) # [800, 7, 5, 3, 2, 1]

# reverse reverse list whatever the data types
myList.reverse()
print(myList) # [['i', 'a', 'new', 'list', 22], 'poe', 'c', 'B', 'A']

# clear
myList.clear()
print(myList) # []

# copy apply shallow copy
mycopy=myList2.copy()
print(myList2) # ['i', 'a', 'new', 'list', 22]
print(mycopy) # ['i', 'a', 'new', 'list', 22]

myList2[0]="i apply change"
print(myList2)  # ['i apply change', 'a', 'new', 'list', 22]
print(mycopy)  # ['i', 'a', 'new', 'list', 22] ---> NOT AFFECRTED

mycopy[0]="This New change "
print(myList2)  # ['i apply change', 'a', 'new', 'list', 22] ----> Not affected
print(mycopy)  # ['This New change ', 'a', 'new', 'list', 22] ---> NOT AFFECRTED


# count count how may times item is exist

# index()
print(mycopy.index("a")) # 1
# print(mycopy.index("eeeea"))  # error as "eeea" is not in the list

# insert (pos , inserted item)  put the item before this pos
mycopy.insert(2,"this inserted item") # ['This New change ', 'a', 'this inserted item', 'new', 'list', 22]
print(mycopy)

# pop
mycopy.pop(1)
print(mycopy) # ['This New change ', 'this inserted item', 'new', 'list', 22]


# tuple
# Tuple items are enclosed in parentheses
# you can remove the parentheses and this still tuple
# tuple are ordered , can use index to access item
# tuple is immutable ---------> can not modify in it
# tuple items is not unique
# tuple can have data in different data types
# operators used

myTuple=(1,2,"salma")
myTuple2=1,2,5
print(type(myTuple)) # <class 'tuple'>
print(type(myTuple2)) # <class 'tuple'>

print(myTuple[0]) # 1
# myTuple[0]="OO" # Tuples don't support item assignment ---> immutable
print(myTuple)

# tuple of one element
type1=(1,)
print(type(type1)) # <class 'tuple'>

# type concatenation
tuple2=(2,5,6)
type1+=tuple2
print(type1) # (1, 2, 5, 6)


# tuple , list , string Repeat(*) ---> * operator
print(type1*3) # (1, 2, 5, 6, 1, 2, 5, 6, 1, 2, 5, 6)


# count count how many time the item is exist

# index()
print(" the index of the 2 is {} ".format(type1.index(2)))  #  the index of the 2 is 1


# tuple destruct

t1=(1,2,3,4)
a,b,_,c=t1;
print(a) # 1
print(b) # 2
print(c) # 4



# set
# set items are enclosed in a curly brackets
# set items are not ordered and not indexed
# set indexing and sclicing can not be done
# set has only immutable data types like numbers and strings and tuples (list and dictionary are not)
# items is unique
myset={1,2,3}
#print(myset[0]) # error can not do indexing

#myset2={1,2,3,[6,7]} # error can not have lists
#print(myset2)

myset3={3,3,4,2,3,1}
print(myset3) # {1, 2, 3, 4}

# set methods

# claer()

myset3.clear()
print(myset3) # set()

# union( can take more than on set )  or | operator

newset={"salma" ,False}
print(myset|newset) # {False, 1, 2, 3, 'salma'}
print(myset.union(newset)) # {False, 1, 2, 3, 'salma'}


# add()
d={1,2,3,4}
d.add("change")
print(d) # {1, 2, 3, 4, 'change'}

# copy shallow copy

# remove & discard
g={1,2,3}
g.remove(1); # {2, 3}
#g.remove(5) # Error
g.discard(2) # {3}
g.discard(5) # Not give error
print(g);

# pop
myset.pop(); # pop randon element as set is not ordered
print(myset)


op1={1,2,3}
op2={3,4,1}

# differance
print(op2.difference(op1)) # {4}

# differance update will make op2 have the difference set
op2.difference_update(op1)
print(op2) # {4}
# update can update with set or list
op1.update(op2)
print(op1) # {1, 2, 3, 4}



# intersection
e={1,2,"x"}
f={"x",2,5}
print(e.intersection(f)) # {2, 'x'}

e.intersection_update(f)
print(e) # {2, 'x'}

# symmetric differance
i={1,5,9,"salma","doaa"}
j={8,9,1,5,"salma","mamdoh"}
print(i.symmetric_difference(j)) # {'doaa', 'mamdoh', 8}
i.symmetric_difference_update(j)
print(i) # {'doaa', 8, 'mamdoh'}


# a.issuperset(b) return true if all elements in set b is exit in set a else retuen false
test4={1,2}
test5={1,2,5,"salma"}
print(test5.issuperset(test4)) # True
print(test4.issuperset(test5)) # False

# part.issubset(whole)
test6={2,"salma"}
print(test6.issubset(test5)) # True
print(test5.issubset(test6)) # False

# isdisjoint

print(test4.isdisjoint(test5)) # False
test7={555}
print(test7.isdisjoint(test5)) # True


# Dictionary
# dict items are in cerly brackets
# dict items are contains keys :value
# dict key need to be immutable => number , string , tuple (list not allowed)
# dict value can have any data type
# dict key need to be unique
# dict is not ordered you access element with key

var = {
    "name":"salma",
    "age": 20,
    ("math","science") : 100
}
print(var) # {'name': 'salma', 'age': 20, ('math', 'science'): 100}

print(var["name"]) # salma
print(var.get("age")) # 20

print(var.keys()) # dict_keys(['name', 'age', ('math', 'science')])
print(var.values()) # dict_values(['salma', 20, 100])

# two dimensional  dict

dict={
    "one": {
        "name":"salma",
        "age": 20
    },
    "two":{
        "name":"OOOOO",
         "age": 20,
        "job":"Programmer"
    },
    "three":"poe"
}

print(dict["one"]["name"]) # salma


# len
print(len(dict)) # 3
print(len(dict["one"])) # 2

# dict methods
# clear()
var.clear()
print(var) # {}

# update by another dict
member={
    "pp":"poe"
}
dict.update(member)
print(dict) # {'one': {'name': 'salma', 'age': 20}, 'two': {'name': 'OOOOO', 'age': 20, 'job': 'Programmer'}, 'three': 'poe', 'pp': 'poe'}
dict.update({"new":50})
print(dict) # {'one': {'name': 'salma', 'age': 20}, 'two': {'name': 'OOOOO', 'age': 20, 'job': 'Programmer'}, 'three': 'poe', 'pp': 'poe', 'new': 50}
dict["newmember"]="newval"
print(dict) # {'one': {'name': 'salma', 'age': 20}, 'two': {'name': 'OOOOO', 'age': 20, 'job': 'Programmer'}, 'three': 'poe', 'pp': 'poe', 'new': 50, 'newmember': 'newval'}


# copy shallow copy

# setdefault search for the key if exist will print its value if not exit will add key with this default value if you don't put a default value will put none
dict.setdefault("year",2023)
print(dict)# {'one': {'name': 'salma', 'age': 20}, 'two': {'name': 'OOOOO', 'age': 20, 'job': 'Programmer'}, 'three': 'poe', 'pp': 'poe', 'new': 50, 'newmember': 'newval', 'year': 2023}
dict.setdefault("testkey")
print(dict) # {'one': {'name': 'salma', 'age': 20}, 'two': {'name': 'OOOOO', 'age': 20, 'job': 'Programmer'}, 'three': 'poe', 'pp': 'poe', 'new': 50, 'newmember': 'newval', 'year': 2023, 'testkey': None}

# popitem() delete last element in the dict
dict.popitem()
print(dict) # {'one': {'name': 'salma', 'age': 20}, 'two': {'name': 'OOOOO', 'age': 20, 'job': 'Programmer'}, 'three': 'poe', 'pp': 'poe', 'new': 50, 'newmember': 'newval', 'year': 2023}

# items
print(dict.items()) # dict_items([('one', {'name': 'salma', 'age': 20}), ('two', {'name': 'OOOOO', 'age': 20, 'job': 'Programmer'}), ('three', 'poe'), ('pp', 'poe'), ('new', 50), ('newmember', 'newval'), ('year', 2023)])

# fromkeys(0
a=("key1","key2")
b="value"
print(dict.fromkeys(a,b)) #dict_items([('one', {'name': 'salma', 'age': 20}), ('two', {'name': 'OOOOO', 'age': 20, 'job': 'Programmer'}), ('three', 'poe'), ('pp', 'poe'), ('new', 50), ('newmember', 'newval'), ('year', 2023)])
{'key1': 'value', 'key2': 'value'}












