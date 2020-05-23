l=list(map(int,input().strip().split()))
n=l[0]
k=l[1]
for i in range(k):
    s=str(n)
    if s[-1]=='0':
        n=n//10
    else:
        n=n-1
print(n)
