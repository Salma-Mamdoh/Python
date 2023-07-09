# --------------- Errors and exception Raising------------
# Exceptions is a runtime error reporting Mechanism
# Exception gives you the Message to understand the problem
# Traceback Gives you the line to look for the code in this line
# Exceptions Have the line to look for the code in this line
# Raise keyword used to raise your own exceptions
"""
x=int(input())
if x<0:
    raise Exception("The number is less than Zero")
    print("this will not be printed as exception")
else:
    print("ok")

"""
# Exception Handling
# Try , Except , Else , Finally

# Try --> Test the code for errors
# Except ---> Handle the errors

# Else ---> if no errors
# Finally ---> Run the code

try:
    number=int(input("write your age: "))

except:
    print("Error enter only int values ")

else:
    print("No errors ")

finally:
    print("this run whatever happens")


try:
    x=int(input("enter number to devide on it "))
    if 10 /x:
        print("succsssful devision")
except ZeroDivisionError:
    print("cannot divide by zero ")

except :
    print("identifier not found")


# example on Exception Handling
the_file=None
the_tries=5
while the_tries > 0:
    try:
        file_name=str(input("Enter the absolute path of file to open it ")).strip()
        the_file=open(file_name,"r")
        print(the_file.read())
        break
    except FileNotFoundError:
        print("File Not found")
        the_tries-=1
    except:
        print("error happen")
        the_tries-=1
    finally:
        if the_file is not None:
            the_file.close()
else:
    print("The tries ended ")

# ----- Type Hinting --------
def say_Hello(name) -> str: # this means this function accept string as a parameter this a hint for developers not restriction on input
    print(f"hallo {name}")

say_Hello("salma")