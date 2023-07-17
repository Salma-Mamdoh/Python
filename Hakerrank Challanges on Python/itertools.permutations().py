# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

lis = input().split()
res = permutations(lis[0], int(lis[1]))
finalres=[]
for i in res:
    st=""
    for j in i:
        st+=j
    finalres.append(st)
    
finalres.sort()
for i in finalres:
    print(i)
