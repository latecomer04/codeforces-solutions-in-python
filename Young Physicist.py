n=int(input())
s1=0
s2=0
s3=0
for i in range(n):
    l=list(map(int,input().strip().split()))
    s1=s1+l[0]
    s2=s2+l[1]
    s3=s3+l[2]

if s1==0 and s2==0 and s3==0:
    print("YES")
else:
    print("NO")
