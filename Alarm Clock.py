t=int(input())
for i in range(t):
    l=list(map(int,input().strip().split()))
    a=l[0]
    b=l[1]
    c=l[2]
    d=l[3]
    if a<=b:
        print(b)
    else:
        n=a-b
        if c<=d:
            print(-1)
        else:
            m=c-d
            if n%m==0:
                z=n//m
            else:
                z=(n//m)+1
            print(b+z*c)
