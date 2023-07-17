# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
k=int(input())
lis=list(map(int,input().split()))
dic=dict(Counter(lis))
for key,value in dic.items():
    if(value!=k):
        print(key)
