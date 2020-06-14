t=int(input())
for _ in range(t):
    a,b,k=map(int,input().strip().split())
    c=k//2
    d=k-c
    print(a*d-b*c)
