# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
first=list(map(int, input().split()))
second=list(map(int, input().split()))
res=product(first,second)
for i in res:
    print(i,end=" ")
