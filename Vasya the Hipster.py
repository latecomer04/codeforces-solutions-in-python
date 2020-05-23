l=list(map(int,input().strip().split()))
a=l[0]
b=l[1]
count=0
cnt=0
x=0
if a<b:
    count=count+a
    b=b-a

    cnt=cnt+b//2
else:
    count=count+b
    a=a-b

    cnt=cnt+a//2
print(count,end=" ")
print(cnt)

