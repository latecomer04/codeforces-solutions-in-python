n=int(input())
l=list(map(int,input().strip().split()))
count=0
a=l.count(4)
b=l.count(3)
c=l.count(2)
d=l.count(1)
count=count+a
if b>=d:
    count=count+b
    d=0
else:
    count=count+b
    d=d-b
if c%2==0:
    x=c//2
    count=count+x
else:
    x=c//2
    count=count+x
    d=d+2
if d%4==0:
    m=d//4
    count=count+m
else:
    m=d//4
    count=count+m+1
print(count)
