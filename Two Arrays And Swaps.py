t=int(input())
for _ in range(t):
    l=list(map(int,input().strip().split()))
    n=l[0]
    k=l[1]
    a=list(map(int,input().strip().split()))
    b=list(map(int,input().strip().split()))
    a.sort()
    b.sort(reverse=True)
    for i in range(k):
        if a[i]<b[i]:
            a[i]=b[i]
        else:
            continue
        
    print(sum(a))
