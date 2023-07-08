# ----------------------------------
# --- Modules --> Built in Modules ---
# -------------------
# Module is a file contain a set of functions
# you can import module in your app to help you
# you can import multiple modules
# you can create your own modules
# Modules saves your time
# -----------------------------

# import main Module
import random
#print(random.random())

#print(dir(random)) # ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_ONE', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_floor', '_index', '_inst', '_isfinite', '_log', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']

print(random.randint(100,99999))


# create your module
import myModule as mm


mm.sayHello("salma")

# Modules & pacjages
# Module is a single file has some function
# Package group or modules
# External packages downloaded from the internet
# You can install Packages with pyrhon Package Manager PIP
import termcolor
import pyfiglet

print(termcolor.colored(pyfiglet.figlet_format("Salma Mamdoh"), color='black'))



# Date & Time

import datetime as dt
print(dt.datetime.now()) # 2023-07-08 03:07:49.217634
print(dt.datetime.now().time()) # 03:16:54.241859
print(dt.datetime.now().year) # 2023
print(dt.datetime.now().month) # 7
print(dt.datetime.now().day) # 8
print(dt.datetime.now().hour) # 3

# print start and end of date
print(dt.datetime.min) # 0001-01-01 00:00:00
print(dt.datetime.max) # 9999-12-31 23:59:59.999999

mybirthday=dt.datetime(2003,4,24)
myage=dt.datetime.now()-mybirthday
print(myage) # 7380 days, 3:19:49.998757
print(myage.days) # 7380


# format Date
# print date as string format
print(mybirthday.strftime("%a")) # Thu
print(mybirthday.strftime("%A")) # Thursday
print(mybirthday.strftime("%b")) # Apr
print(mybirthday.strftime("%B")) # April

print(mybirthday.strftime("%d - %B - %Y")) # 24 - April - 2003


