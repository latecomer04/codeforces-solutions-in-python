n=int(input())
l=list(map(int,input().strip().split()))
m=int(input())
arr=list(map(int,input().strip().split()))
l.sort()
arr.sort()
count=0
if n<m:
    for i in range(n):
        for j in range(m):
            if abs(l[i]-arr[j])==1 or abs(l[i]-arr[j])==0:
                count=count+1
                l[i]=-2
                arr[j]=-2
                break

else:
    for i in range(m):
        for j in range(n):
            if abs(arr[i]-l[j])==1 or abs(arr[i]-l[j])==0:
                count=count+1
                arr[i]=-2
                l[j]=-2
                break
print(count)
