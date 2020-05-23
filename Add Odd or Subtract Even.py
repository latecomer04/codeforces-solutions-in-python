t=int(input())
for i in range(t):
    l=list(map(int,input().strip().split()))
    a=l[0]
    b=l[1]
    if a<b:
        if a%2!=0 and b%2!=0:
            print(2)
        elif a%2==0 and b%2==0:
            print(2)
        elif a%2==0 and b%2!=0:
            print(1)
        else:
            print(1)
    elif a==b:
        print(0)
    else:
        if a % 2 != 0 and b % 2 != 0:
            print(1)
        elif a % 2 == 0 and b % 2 == 0:
            print(1)
        else:
            print(2)
