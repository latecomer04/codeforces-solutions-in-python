l=list(map(int,input().strip().split()))
l.sort()
count=0
a=l[1]
count=count+abs(l[1]-l[0])
count=count+abs(l[2]-l[1])
print(count)
