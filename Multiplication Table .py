l=list(map(int,input().strip().split()))
n=l[0]
x=l[1]
count=0
for i in range(1,n+1):
    if x%i==0:
        a=x//i
        if a<=n:
            count=count+1
print(count)
