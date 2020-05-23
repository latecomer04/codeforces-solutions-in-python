n=int(input())

for i in range(n):
    arr=list(map(int,input().strip().split()))
    a=arr[0]
    b=arr[1]
    if a%b==0:
        print(0)
    else:
        c=a//b+1
        b=c*b
        print(b-a)
