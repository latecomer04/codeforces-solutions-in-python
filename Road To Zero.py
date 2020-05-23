t=int(input())
for i in range(t):
    l=list(map(int,input().strip().split()))
    x=l[0]
    y=l[1]
    arr=list(map(int,input().strip().split()))
    a=arr[0]
    b=arr[1]
    m=10**19
    if x==y and x>0:
        m=min(m,x*b)
        m=min(m,(x+y)*a)
        print(m)
    elif x==y and x==0:
        print(0)
    elif x>y or y>x:
        p=x*a+y*a
        q=abs(x-y)*a+min(x,y)*b
        m=min(p,q)
        print(m)
