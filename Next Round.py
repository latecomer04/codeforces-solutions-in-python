l=list(map(int,input().strip().split()))
a=list(map(int,input().strip().split()))
k=l[1]-1
n=l[0]
compare=a[k]
count=0

for i in range(n):
    if a[i]>=compare:
        if a[i]>0:
            count=count+1
        else:
            break
print(count)
