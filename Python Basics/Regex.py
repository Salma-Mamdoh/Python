# Regular Expressions
# sequance of characters that define a search pattern
# used in validation
# to test regex https://pythex.org/
# cheat of regex https://www.debuggex.com/cheatsheet/regex/python
# https://regex101.com/
# Quantifiers
# -----------
# * 0 or more
# + 1 or more
# ? 0 or 1
# {2} Exactly 2
# {2,5} Between 2 and 5
# {,5} up to 5
# {2,} 2 or more
# --------------

# Character classes
# -----------
# [0-9]
# [^0-9]
# [A-Z]
# [^A-Z]
# [a-z]
# [^a-z]
# ----------
# Assertions
# ------------
# ^ start of string
# $ End of string
# -------------

# Logical or And Escaping
# ------------------
# | or
# \ Escape sepcial charachers
# () seperate Groups
# -----------------

# search()  => Search A string For a match and return a first Match only
# finalall() => returns a list of all matches and empty list if no match

# Email validation pattern => [A-z0-9\.]+@+[A-z0-9]+\.(com|org|net)

import re # to user regex
mystring=re.search(r"[A-Z]","Salma")
print(mystring) # <re.Match object; span=(0, 1), match='S'>  span ----> pos of matched string



is_email=re.search(r"[A-z0-9\.]+@+[A-z0-9]+\.(com|org|net)","smmdwh985@gmail.com")
if(is_email):
    print("This a valid email")
else:
    print("Not valid email")

email_inp=input("Please Enter your Email")
search=re.findall(r"[A-z0-9\.]+@+[A-z0-9]+\.com|org|net",email_inp)

mylist=[]
if search !=[]:
    print("Valid Emial")
else:
    print("NOt Valid Email")
mylist.append(search)
for email in mylist:
    print(email)

# output
# Valid Emial
# ['smmdwh985@gmail.com']

# split (pattern , string , maxsplit) => return a list of elements splited on each match
# sub ( pattern , replace , string , replacecount) => replace matches with what you want

string_one="I love c++ more than pyhton"

search_one=re.split("\s",string_one)

search_two=re.split("\s",string_one, 1)

print(search_one) # ['I', 'love', 'c++', 'more', 'than', 'pyhton']
print(search_two) # ['I', 'love c++ more than pyhton']

string_three="How_to write a very-good # atricle" # ['How', 'to', 'write', 'a', 'very', 'good', '', '', 'atricle']
se=re.split("_|-|\s|#",string_three)

print(se)

string_one=re.sub("\s","_",string_one)
print(string_one) # I_love_c++_more_than_pyhton

# Group traning and flags flags like ignore case or dot all , multple lines 
# (.)+  match all characters except the newline

myweb="https://www.elzero.com"
searchweb=re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)",myweb,re.I)

print(searchweb.group()) # https://www.elzero.com
print(searchweb.groups()) # ('https', 'www', 'elzero', 'co', None, 'm')