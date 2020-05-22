l=list(map(int,input().strip().split()))
n=l[0]
t=l[1]
a=int(str(1)+"0"*(n-1))
b=int("9"*(n))
flag=0
for i in range(a,b+1):
    if i%t==0:
        print(i)
        flag=1
        break
if flag==0:
    print(-1)
