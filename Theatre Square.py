arr=list(map(int,input().strip().split()))
n=arr[0]
m=arr[1]
a=arr[2]

b=max(m,n)
c=min(m,n)
if a==1:
        print(m*n)
else:
        i=1
        while a*i<b:
            i=i+1
        j=1
        while a*j<c:
            j=j+1
        if j==1:
            print(i)
        else:
            print(i*j)
