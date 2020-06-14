t=int(input())
for _ in range(t):

    n,m=map(int,input().strip().split())
    if n==1 or m==1:
        print("YES")
    elif n==m and n==2:
        print("YES")
    else:
        print("NO")
