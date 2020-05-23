t=int(input())
for _ in range(t):
    n=int(input())
    if n==1:
        print(0)
    else:
        a=(n-1)//2
        b=a*(a+1)*((2*a)+1)
        print((8*b)//6)
