def func():
    l=list(map(int,input().strip().split()))
    l.sort()
    a=l[0]
    b=l[1]
    c=l[2]
    d=l[3]
    print(d-a,end=" ")
    print(d-b,end=" ")
    print(d-c,end=" ")
func()
