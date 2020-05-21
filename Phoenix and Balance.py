t=int(input())
for i in range(t):
    n=int(input())
    a=2**n
    for j in range(n//2-1):
        a=a+2**(j+1)
    b=0
    for j in range(n//2,n):
        b=b+2**(j)
    print(abs(a-b))
