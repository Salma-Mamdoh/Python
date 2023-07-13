from collections import defaultdict
n, m = input().split()
dic = defaultdict(list)

for i in range(int(n)):
    x = input()
    dic[x].append(i + 1)

for i in range(int(m)):
    x = input()
    res = []
    if x in dic:
        print(" ".join(str(i) for i in dic[x]))
    else:
        print(-1)
