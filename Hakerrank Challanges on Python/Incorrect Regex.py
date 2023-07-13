# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
t=int(input())
for i in range (0,t):
    inp=str(input())
    try:
        pattern=re.compile(inp)
        print("True")
    except:
        print("False")
