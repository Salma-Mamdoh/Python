print("hallo") # can write ; if you want to write 2 statements in the same line
print("salma")
# python indentation is sensative  language
# All data types in python are objects
# variable can only start (A-Z) or (a-z) or _
# variables name can not have special characters
# variables name can not start with number but can include numbers and _ (can start with _)
# concatination
msg="salma"
lname="mamdoh"
print(msg+" "+lname+"\n" + "Sabry")
# can not concatenate string + int only string + string

# to make multiple line string
str="salma \
mamdoh \
sabry"
print(str) # salma mamdoh sabry

# strings ss1 and ss2 the same
ss1="Salma Mamdoh"
ss2='Salma Mamdoh'
# with escape char
ss3='Salma "Mamdoh"' # Salma "Mamdoh"
ss4="Salma 'Mamdoh'" # Salma 'Mamdoh'
ss5='salma \'Mamdoh\''# salma 'Mamdoh'
print(ss1,ss2,ss3,ss4,ss5)
multistring=""" my name is salma 
how are you 'dooooooo'
"""
print(multistring)

# indexing
indexs="Hallo world"
print(indexs[0])
print(indexs[-1])
print(indexs[0:5])  # [start:end]   or [start,end,steps]
# note end not includeing
print(indexs[:]) # print Hallo world

print(indexs[::2]) # 2 here is num of steps

# string methods
newstr="            salma       Mamdoh     "
print(len(indexs)) # return length or str
print(len(newstr)) # will count space as a char

# strip function to delete spaces
print(newstr.strip()) # delete spaces from left and right Not middle
print(len(newstr.strip()))
print(newstr.lstrip())  # delete spaces from left only
print(len(newstr.lstrip()))
print(newstr.rstrip()) # delete spaces from right only
print(len(newstr.rstrip()))

# title method convert first char of each word to capital and the words after numbers
ww="joe how are 4you "
print(ww.title())
# captalize method converts only first char of only first word to capital word
print(ww.capitalize())
# upper method convert all string to upper case
print(ww.upper())
# lower method convert all string to lower case
print(ww.lower())
# z fill method this method filles the start of string with zeros to be with length which passed as a parameter to function
a,b,c,d="1","11","111","1111"
print(a.zfill(4)) # 0001
print(b.zfill(4)) # 0011
print(c.zfill(4)) # 0111
print(d.zfill(4)) # 1111

# split function split(seperator) or split(seperator,max_split)
trysplit="i-love-python-and-c++"
print(trysplit.split("-",2)) # ['i', 'love', 'python-and-c++']
print(trysplit.rsplit("-",2)) # ['i-love-python', 'and', 'c++']

# center makes string in the senter and add chars from lest and right to reach specific length passed in paramter
e="Salma"
print(e.center(9)) # by default will add spaces
print(e.center(9,'*')) # **Salma**
print(e.center(9,"#")) # ##Salma##

# count count how many times this string or this char is exist in ths string passing them with ""
f="i love python and c++ ,but c++ more "
print(f.count("c++"))
print(f.count("o"))
print(f.count("o",0,10)) # can takes start && end

# swapcase swap upper case to lower case and the opposite
d="SalmA Mamdoh R"
print(d.swapcase())  # sALMa mAMDOH r

# startswith() && endswith() -----> Return true or false
g="I love Python"
print(g.startswith("I")) # true
print(g.startswith("P")) # false
print(g.startswith("P",7,)) # true
print(g.endswith("n")) # true


# index() search for a index of the string
print(g.index("P")) # 7
# print(g.index("P",0,5)) # will get error

# find same as index but don't give error if char ( substr) not exist ---> get -1
print(g.find("P")) # 7
print(g.find("P",0,5)) #-1

# rjust(width , fill char) &&  ljust(width , fill char) default fillchar is space
print(g.ljust(30)) # 30 is the length you want
print(g.ljust(30,'#'))  # I love Python#################

print(g.rjust(30,"#")) # #################I love Python

# splitlines() return list of lines

# can do multiple lines by this way or by using "\n"
str6="""salma 
mamdoh 
sabry 
"""
print(str6.split()) # ['salma', 'mamdoh', 'sabry']

# expandtabs()
test="Salma\tMamdoh\tSabry"
print(test) # Salma	Mamdoh	Sabry
print(test.expandtabs(5)) # Salma     Mamdoh    Sabry


# mehods return bool
tes="I am not  a tiile 5p";
test2="I Am  A Tite 5P"
print(tes.istitle()); # FALSE
print(test2.istitle()) # TRUE

OO=" "
print(OO.isspace()) # true

# islower check all chars is string is lowers

# isidentifier check if this name is valid to be variable name or not

# isalpha check if all chars in the string is alphapiticals
# isalnum checks if string have chars and numbers

quu="aaa123"
print(quu.isalpha()); #false
print(quu.isalnum()) # true


# replce(old value , new value , count)
eee="hallo one two and one one "
print(eee.replace("one","five")) # hallo five two and five five
print(eee.replace("one","five",2)) # hallo five two and five one

# seperator.join (iterable) ---> joins elements of the list or tuple in a string
mylist=["salma","mamdoh","sabry"]
print("_".join(mylist)) # salma_mamdoh_sabry


# string formating ( OLD WAY)
# print("salma" + 5) # error can not concatonate string with int
# ---> use palceholder to avoid this error
testname="Salma"
age=20
rank=1
print("My name is : %s"% "salma")
print("My name is : %s"% testname)
print("My name is : %s and my age is : %d  and my rank is %f "%(testname,age,rank))
# %s --->string
# %d ----> number
# %numofnumbersafterpointf liks .2f ----> float


# truncate string
lasttest="Hallo i am salma i love myself"
print("Message is %.5s"%lasttest) # Message is Hallo  ---> 5 is the number of chars you want


# string formating 2 (NEW WAY)
print("My name is : {}".format("salma"))
print("My name is : {}".format(testname))
print("My name is : {:s} and my age is : {:d}  and my rank is {:f} ".format(testname,age,rank))

# format Money
mymoney=123425786
print(" My Money In Bank is : {:_d}".format(mymoney))


aa,bb,cc="one","two","three"
print("Hallo {2} {0} {1} ".format(aa,bb,cc))
print("Hallo {2:s} {0:s} {1:s} ".format(aa,bb,cc))


# format in version 3.6+
myname="salma"
myage=20
print("my name is {myname} and my age is {myage}")
print(f"my name is {myname} and my age is {myage}")

