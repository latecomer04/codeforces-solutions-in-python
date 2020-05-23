t=int(input())
for i in range(t):
    n=int(input())
    a=n//2
    if a%2!=0:
        print("NO")
    else:
        l=[0]*n
        for j in range(1,n//2+1):
            l[j-1]=j*2
        for k in range(n//2+1,n):
            l[k-1]=2*(k-n//2)-1
        b=a//2
        b=b+1
        l[n-1]=l[-2]+b*2
        print("YES")
        for x in l:
            print(x,end=" ")
        print()
