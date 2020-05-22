t=int(input())
for i in range(t):
    count=0
    l=list(map(int,input().strip().split()))
    a=l[0]
    b=l[1]
    c=l[2]
    d=max(a,b,c)
    count=count+d-a+d-b+d-c
    n=l[3]
    n=n-count
    if n>=0 and n%3==0:
        print("YES")
    else:
        print("NO")
