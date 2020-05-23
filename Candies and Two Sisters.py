n=int(input())
for i in range(n):
    a=int(input())
    if a%2==0:
        b=a//2-1
        if b>0:
            print(b)
        else:print(0)
    else:
        b=a//2
        if b>0:print(b)
        else:print(0)
