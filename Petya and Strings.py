s1=input()
s2=input()
l1=list(s1)
l2=list(s2)
for i in range(len(s1)):
    if 65<=ord(l1[i])<=90:
        l1[i]=chr(ord(l1[i])+32)
    if 65<=ord(l2[i])<=90:
        l2[i]=chr(ord(l2[i])+32)
flag=0
for i in range(len(l1)):
    if l1[i]>l2[i]:
        flag=1
        print(1)
        break
    elif l1[i]<l2[i]:
        flag=1
        print(-1)
        break
if flag==0:
    print(0)
