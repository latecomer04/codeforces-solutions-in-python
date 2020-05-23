n=int(input())
l = list(map(int, input().strip().split()))
a=max(l)
count=0
for i in l:
    b=a-i
    count=count+b
print(count)
