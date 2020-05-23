import math
t=int(input())

for x in range(t):
    flag=0
    l=list(map(int,input().strip().split()))
    a=l[0]
    n=l[1]
    m=l[2]
    if 10*m>=a:
        print("YES")
    else:
        for i in range(n):
            a=math.floor(a/2)+10

            if  a<=0:
                print("YES")
                flag=1
                break
        if flag==0:
            if 10*m>=a:
                print("YES")
                flag=1

        if flag==0:
            print("NO")
