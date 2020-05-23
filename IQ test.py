n = int(input())
arr = list(map(int, input().strip().split()))
odd = 0
even = 0
for i in range(n):
    if arr[i]%2==0:
        arr[i]=0
    else:
        arr[i]=1
a=arr.count(0)
b=arr.count(1)
if a>b:
    print(arr.index(1)+1)
else:
    print(arr.index(0)+1)
