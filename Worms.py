n=int(input())
l=list(map(int,input().strip().split()))
m=int(input())
arr=list(map(int,input().strip().split()))
a=[]
for i ,x in enumerate(l):
    for _ in range(x):
        a.append(i+1)
for j in arr:
    print(a[j-1])
