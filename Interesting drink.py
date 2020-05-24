import bisect
n=int(input())
l=list(map(int,input().strip().split()))
l.sort()
m=int(input())
for i in range(m):
    a=int(input())
    print(bisect.bisect(l,a))
