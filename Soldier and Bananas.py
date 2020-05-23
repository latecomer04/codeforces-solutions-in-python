n=int(input())
m=0
count=0
for _ in range(n):
    l=list(map(int,input().strip().split()))
    a=l[0]
    b=l[1]
    count=count-a+b
    m=max(m,count)
print(m)
