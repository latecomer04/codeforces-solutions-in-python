n=int(input())
l=list(map(int,input().strip().split()))
a=max(l)
b=min(l)
m=l.index(a)
p=0
for i in range(n):
    if l[i]==b:
        p=i
count=0
if p>m:
    count=count+m
    count=count+(n-1-p)
else:
    count=count+m
    count=count+(n-1-p-1)
print(count)
