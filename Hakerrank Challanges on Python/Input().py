# Enter your code here. Read input from STDIN. Print output to STDOUT
x, K = input().split()
st = input()
res = eval(st, {'x': int(x)})

if res == int(K):
    print("True")
else:
    print("False")
