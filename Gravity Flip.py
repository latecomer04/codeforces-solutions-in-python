n=int(input())
l=list(map(int,input().strip().split()))
l.sort()
for i in l:
    print(i,end=" ")
