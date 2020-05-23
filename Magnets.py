n=int(input())
l=[]
m=1
for i in range(n):
    s=input()
    l.append(s)
    if i>0:
        count=1
        if l[i-1]==l[i]:
            count=count+1
        else:
            m=m+1
            count=1
print(m)
