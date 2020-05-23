n=int(input())
count=0
for _ in range(n):
    arr=list(map(int,input().strip().split()))
    if arr.count(1)>=2:
        count=count+1
print(count)
