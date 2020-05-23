n=int(input())
s=input()
c=input()
count=0
for i in range(n):
    a=int(s[i])
    b=int(c[i])
    d=abs(a-b)
    e=min(a,b)
    f=max(a,b)
    e=e+10
    cnt=abs(f-e)
    count=count+min(cnt,d)
print(count)
