# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

st = input().strip()
for i, group in groupby(st):
    count = sum(1 for _ in group)
    print(f"({count}, {i})", end=" ")
