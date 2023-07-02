# BOOLEAN --> true or false
print(bool("salma")) # true
print(bool(100)) # true
print(bool([1,2,3])) # true

print(bool([])) # False
print(bool(0)) # False
print(bool("")) # False
print(bool(False)) # False
print(bool(())) # False
print(bool(None)) # False

# boolean operator ---> and , or , not


# Assignment operator = , += , -=, /= , **= , %= , //=

# Comparison operators == , != , > , < ,>= , <=

# Type conversion
# str() ---> convert to strong
# tuple() ---> convert to tuple
# list() ---> convert to list
# set() ---> convert to set
# dict ---> convert to dictionary must have key and value to allow conversion can do this with tuple and list
# NOTE -----------> set can not be converted to dict as you can not do nested sets in the set
d=(("a",1),("c",2))
print(dict(d)) # {'a': 1, 'c': 2}


# User input
"""
fname=input("enter your first name ")
middle=input("enter your middle name")
age=input("enter your age")
# putting one more methid for same variable called chain method
fname=fname.strip().capitalize()
middle=middle.strip().capitalize()
age=middle.strip().capitalize()
print(f"your first name is {fname} and your middle name is {middle:.1s} and your age is {age}")
"""

# practical email slice
"""
email=input("enter your email")
email=email.strip()
x=email.index("@")
username=email[:x]
y=email.index(".")
y+=1
website=email[y:]

print(f"your username is {username} \n your website is {website}")
"""


# practical your age full details
"""
age=int(input("enter your age"))

# get age in all time units
months=age*12

weeks=months*4

days=weeks*7

hours=days*12

minutes=hours*60

seconds=minutes*60

print(f"your age in years is {age} year \n your age in weeks {weeks} week \n your age in days {days:,} day \n your age in hours {hours:,} hour \n your age in minutes {minutes:,} minute\n your age in seconds {seconds:,} second \n")

"""


# Control flow
"""
age = int(input("enter your age"))
gender=(input("enter M or F"))
if age == 20 and gender == "F":
    print("your are so pretty ")
    hobby=input("entet your hobby")
    if hobby=="football" or hobby=="basket":
        print("nice hobby")
elif age<10 :
    print("you are so young ")
else:
    print("you are old")
"""

# ternary if
# result if true "if"  condition "else" res if not true
country="Egypt"

print("Your are Egyptian" if country == "Egypt" else print("You are not Egyptian"))


# Calculate age advanced version
"""
age=int(input("enter your age "))

option=int(input("For weeks enter 1 \nFor days enter 2\nFor hours enter 3"))

weeks=age*12*4
days=weeks*7
hours=days*24

if option==1 :
    print(f"{weeks} week")
elif option==2 :
    print(f"{days} day")
elif option==3 :
    print(f"{hours} hour")
else:
    print("this not option")

"""


# membership operators
# in  ----> good with containers like  list
"""
testname = "Salma Mamdoh"
print("s" in testname) # false
print("M" in testname) # true
print("a" in testname) # true
print("p" in testname) # false

# practical Membership Control
admin=["Salma","Mamdoh","Rahma"]
name=input("Enter your name ")
name=name.strip().capitalize()
if name in admin :
    print("looggened successfully")
    opt=int(input(" for delete enter 1 \nfor update enter 2"))
    if opt == 1:
        admin.remove(name)
        print(admin)
    elif opt== 2:
        newname=input("enter new name").strip().capitalize()
        inde=admin.index(name)
        admin[inde]=newname
        print(admin)
    else :
        print("invalid option")
else :
    print("you are not admin")
    status=input("if you want to be admin enter Y else N").strip().capitalize()
    if status == "Y" :
        adminname = input("Enter your name ").strip().capitalize()
        admin.append(adminname)
        print(admin)
    else :
        print("You are not added")
"""


 # Loop
# While loop
"""
a=0
while a <10 :
    print(a)
    a+=1
else :
    print("loop is done ")

mylist2=[1,2,3,4,5,6,7,8,9,10,11]
indexofitem=0
while indexofitem < len(mylist2) :
    print(f"#{str(indexofitem+1).zfill(2)} {mylist2[indexofitem]}")
    indexofitem+=1


# simple bookmark manager
websites=[]
maxsize=5
while maxsize>0:
    webname=input("enter the website namw").strip()
    websites.append(f"https://{webname.lower()}.com")
    maxsize -= 1
    print(f"website added and there are {maxsize} left")
    print(websites)
else :
    print("Book mark is full")

if len(websites) >0 :
    websites.sort()
    print("i will print the list")
    index =0;
    while index < len(websites):
        print(f"#{str(index+1)} {websites[index]}")
        index+=1

"""

# password guess
"""
tries=4
mainpass="salma123"
inputpass=input("enter the password").strip()

while mainpass != inputpass and tries>0 :
    tries -= 1
    print(f"Wrong password and you have {'last chance 'if tries == 1 else tries } chances left")
    inputpass = input("enter the password").strip()
else :
    if mainpass == inputpass :
        print("Successful")
    else :
        print(" NOt successful")
"""

# for loop
"""
mynumbers=[1,2,3,5,6]
for number in mynumbers :
    print(number)

for  number in range(1,20) :
    print(number)
    """

myskills={
    "c++":"90%" ,
    "python" :"50%"
}
for oo in myskills:
    print(f"{oo} {myskills[oo]}")
for key in myskills.keys():
    print(key)

for val in myskills.values():
    print(val)

for item in myskills.items(): #('c++', '90%')
                             # ('python', '50%')
    print(item)


# nested loop

peoples={
    "salma":{
        "c++":"90%" ,
        "python" :"50%",
        "js" :"40%"
    },
    "Ahmed":{
        "css":"100%",
        "html":"10%"
    }
}
for key in peoples:
    print(f"the skills of person {key} is")
    for skill in peoples[key]:
        print(f"{skill} {peoples[key][skill]}")


# break , continue , pass

# Advances dict loop
for key , value in peoples.items():
    print(f"{key} => {value}")
# output
# salma => {'c++': '90%', 'python': '50%', 'js': '40%'}
# Ahmed => {'css': '100%', 'html': '10%'}

for key, value in peoples.items():
    print(f"{key} => ")
    for mkey,mval in value.items() :
        print(f"{mkey} => {mval}")


# Function
# a function is a reuasble block of code to do a task
# a function run when you call it
# a function  accept element to deal with called parameters
# a function can do task without returning data
# a function create to prevent dry --- don't repear yourserlf
# a function accepst elements when you call it called [arguments]
# there is a built in functions and user defiend functions
# a function is for all team and all apps

def say_hallo(name): # name is parameter
    print(f"hallo {name}")

list55=["salma" , "Ahmed"]
for per in list55 :
    say_hallo(per) # per is argument

# function packing and unpacking arguments  * unpack

def say(*ll): # name is parameter
    print(type(ll)) # tuple
    for name in ll:
        print(f"hallo {name}")

say("salma" , "Ahmed","ooo","pp","uuuu") # can add any number of arguements

nlist=[1,2,3,4,5]
print(nlist) # [1, 2, 3, 4, 5]
print(*nlist) # 1 2 3 4 5

# Note default parameter must be the last paramneter or all prameter after this parameter have default value
# default paramenters
def hallo(name,age=20):
    print(f"hallo {name} and your age {age}")

hallo("hallo",20)
hallo("doaa")

# function packing and unpACKING ARGUMENTS **KEYWORD ARGS
def show_skill(**skills):
    print(type(skills)) # dict
    for skill,value in skills.items():
        print(f"skill=>{skill} =>{value}")


show_skill(html="80%" , css="20%") # can pass dict to function like this **dictname


# function scope
"""
yy=1 # global scope

def chance():
    yy=2 # not global his scope inside function 
    print(yy)

chance() # 2
print(yy) #1
"""

xx=1
def one():
    global xx
    xx=17
    print(xx)


print(xx) #1
one() #17
print(xx) # 17 override by using global


# recursion
def cleanstring(str):
    if len(str)==1:
        return str
    elif str[0]==str[1]:
        return cleanstring(str[1:])
    else:
        return str[0]+cleanstring(str[1:])

print(cleanstring("wwwooorrrlllllld"))


# lambda function
# lambda name has no name
# you can call it inline without defining it
# you can use it in return data from another function
# Lambda used for simple functions and def handle the large tasks
# lambda is one single line expression not block of code
# lamda type is function


def sayhello(name):
    print(f"hallo{name}")

sayhello("salma") # hallosalma

hellolambda= lambda name: f"hallo in lambda function{name}"

print(hellolambda("koko")) # hallo in lambda functionkoko

print(sayhello.__name__) # sayhello
print(hellolambda.__name__) #<lambda>














