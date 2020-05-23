n=int(input())
l=[]
for i in range(n):
    arr=list(map(int,input().strip().split()))
    l.append((arr[0],arr[1]))
count=0
for i in range(n-1):
    for j in range(i+1,n):
        if l[i][1]==l[j][0]:
            count=count+1
        if l[i][0]==l[j][1]:
            count=count+1
print(count)
