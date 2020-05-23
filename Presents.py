n=int(input())
arr=list(map(int,input().strip().split()))
l=[]
for i in range(n):
    l.append((arr[i],i+1))

l.sort()

for i in l:
    print(i[1],end=" ")
