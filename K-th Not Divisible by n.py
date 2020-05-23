import math
t=int(input())
for _ in range(t):
    l=[]
    arr=list(map(int,input().strip().split()))
    n=arr[0]
    k=arr[1]
    need=math.floor((k-1)/(n-1))
    print(need +k)
