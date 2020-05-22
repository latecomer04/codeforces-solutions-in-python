n=int(input())
l=[]
flag=0
for i in range(n):
    s=input()
    if flag==0:
        if "OO" in s:
            s=s.replace("OO","++",1)
            flag=1
    l.append(s)
if flag==0:
    print("NO")
else:
    print("YES")
    for i in l:
        print(i)
