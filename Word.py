s=input()
l=list(s)
caps=0
small=0
for i in s:
    if 65<=ord(i)<=90:
        caps=caps+1
    else:
        small=small+1
if caps>small:
    for i in range(len(l)):
        if 97<=ord(l[i])<=122:
            l[i]=chr(ord(l[i])-32)
    print("".join(str(e) for e in l))

else:
    for i in range(len(l)):
        if 65<=ord(l[i])<=90:
            l[i]=chr(ord(l[i])+32)
    print("".join(str(e) for e in l))
