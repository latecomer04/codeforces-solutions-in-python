n=int(input())
l=list(map(int,input().strip().split()))
m=0
count=1
flag=0
if n==1:
    print(1)
else:
    for i in range(n-1):
        if l[i]<=l[i+1]:
            count=count+1
            if i==n-2:
                print(max(m,count))
                flag=1
                break
        else:
            m=max(m,count)
            count=1
    if flag==0:
        print(m)
