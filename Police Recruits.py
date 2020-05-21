t=int(input())
l=list(map(int,input().strip().split()))
a=0
for i in range(t):
    if l[i]>0:
        a=a+l[i]
    else:
        if a>0:
            l[i]=l[i]+1
            a=a-1
print(l.count(-1))
