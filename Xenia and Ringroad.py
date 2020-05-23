arr=list(map(int,input().strip().split()))
n=arr[0]
m=arr[1]
l=list(map(int,input().strip().split()))
count=l[0]-1
for i in range(1,m):
    if l[i]>=l[i-1]:
        count=count+l[i]-l[i-1]
    else:
        count+=n+l[i]-l[i-1]
print(count)
