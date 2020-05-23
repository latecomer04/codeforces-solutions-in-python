t=int(input())
for _ in range(t):
    l=list(map(int,input().strip().split()))
    n=l[0]
    m=l[1]
    if n==1:
        print(0)
    elif n==2:
        print(m)
    else:
        print(2*m)
