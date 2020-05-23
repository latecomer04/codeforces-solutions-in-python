l = list(map(int, input().strip().split()))
n=l[0]
k=l[1]
a=240-k
count=0
i=1
while a>=i*5 and i<=n:
    a=a-i*5
    i=i+1
    count=count+1
print(count)
