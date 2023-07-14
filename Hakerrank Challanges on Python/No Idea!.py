n, m = map(int, input().split())
arr = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))

happ=0
for i in arr:
    if i in a:
        happ+=1
    elif i in b:
        happ-=1
        
print(happ)
