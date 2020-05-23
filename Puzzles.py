l=list(map(int,input().strip().split()))
n=l[0]
m=l[1]
f=list(map(int,input().strip().split()))
if n==m:
    print(max(f)-min(f))
else:
    count = 10 ** 10
    f.sort()
    for i in range(0, m-n+1):
        a = f[i]
        b = f[i+n-1]
        count = min(count, (b - a))
    print(count)
