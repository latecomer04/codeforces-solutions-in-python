arr=list(map(int,input().strip().split()))
l=list(map(int,input().strip().split()))

l.sort()
m=0
if 0 not in l:
    m=max(m,l[0])

if arr[1] not in l:
    m=max(m,arr[1]-l[-1])

for i in range(len(l)-1):
    a=l[i+1]-l[i]
    m=max(m,a/2)
print(m)
