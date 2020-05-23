n=int(input())
l=list(map(int,input().strip().split()))
l.sort(reverse=True)
for i in range(n):
    a=l[0:i+1]
    b=l[i+1:]
    if sum(a)>sum(b):
        print(len(a))
        break
