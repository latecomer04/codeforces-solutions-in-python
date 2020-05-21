t=int(input())
for i in range(t):
    n=int(input())
    for k in range(2,30):
        a=2**k-1
        if n%a==0:
            print(n//a)
            break
