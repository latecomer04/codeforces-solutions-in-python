import math
a1,a2,a3=map(int,input().strip().split())
b1,b2,b3=map(int,input().strip().split())
n=int(input())
count=0
sa=a1+a2+a3
sb=b1+b2+b3
count=count+math.ceil(sa/5)
count=count+math.ceil(sb/10)
if count<=n:
    print("YES")
else:
    print("NO")
