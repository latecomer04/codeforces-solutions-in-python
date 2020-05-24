import math
t=int(input())
for _ in range(t):
    l=list(map(int,input().strip().split()))
    n=l[0]
    k=l[1]
    ans=n
    for i in range(1,1+int(math.sqrt(n))):
        if n%i==0:
            if i<=k:
                ans=min(ans,n//i)
            if n//i<=k:
                ans=min(ans,i)
    print(ans)
