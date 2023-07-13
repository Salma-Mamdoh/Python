# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for i in range(t):
    try:
        num = list(map(int, input().split()))
        print(num[0] // num[1])
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:",e)
