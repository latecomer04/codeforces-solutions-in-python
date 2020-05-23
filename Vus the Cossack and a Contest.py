l=list(map(int,input().strip().split()))
n=l[0]
m=l[1]
k=l[2]
x=min(k,m)
if x>=n:
    print("yes")
else:print("no")
