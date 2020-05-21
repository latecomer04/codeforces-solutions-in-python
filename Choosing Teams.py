l=list(map(int,input().strip().split()))
arr=list(map(int,input().strip().split()))
n=l[0]
k=l[1]
count=0
for i in arr:
    if i<=5-k:
        count=count+1
print(count//3)
