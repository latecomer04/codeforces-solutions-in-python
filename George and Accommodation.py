n=int(input())
count=0
for i in range(n):
    l=list(map(int,input().strip().split()))
    p=l[0]
    q=l[1]
    if q-p>=2:
        count=count+1
print(count)
