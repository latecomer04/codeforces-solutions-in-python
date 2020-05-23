l=list(map(int,input().strip().split()))
n=l[0]
k=l[1]
if n%2==0:
    if n//2>=k:
        print(2*k-1)
    else:
        print(2*(k-n//2))
else:
    if n//2+1>=k:
        print(2*k-1)
    else:
        print(2*(k-(n//2+1)))
