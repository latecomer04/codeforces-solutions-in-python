n=int(input())
l=list(map(int,input().strip().split()))
for i in range(n):
    l[i]=l[i]/n
print(sum(l))
