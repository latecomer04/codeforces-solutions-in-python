l=list(map(int,input().strip().split()))
n=l[0]
m=l[1]
arr=[]
for i in range(n):
    a=[]
    for j in range(m):
        a.append("#")
    arr.append(a)

for i in range(1,n,2):
    a=i//2
    if a%2==0:
        for j in range(m-1):
            arr[i][j]="."
    else:
        for j in range(1,m):
            arr[i][j]="."
for i in range(n):
    for j in range(m):
        print(arr[i][j],end="")
    print()
