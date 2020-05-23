a=input()
b=input()
c=input()
l=list(c)
flag=0
for i in a:
    if i in l:
        l.remove(i)
    else:
        print("NO")
        flag = 1
        break


if flag==0:
    for i in b:
        if i in l:
            l.remove(i)
        else:
            print("NO")
            flag=1
            break
if flag==0:
    if len(l)==0:
        print("YES")
    else:
        print("NO")
