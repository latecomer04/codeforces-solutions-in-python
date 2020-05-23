s=input()
l=list(s)
if 65<=ord(s[0])<=90:
    flag=0
    for i in range(1,len(s)):
        if 65 <= ord(s[i]) <= 90:
            continue
        else:
            flag=1
            break
    if flag==0:
        for i in range(len(s)):
            l[i]=chr(ord(l[i])+32)
        print("".join(str(e) for e in l))
    else:
        print(s)
else:
    if 97<= ord(s[0]) <=122:
        flag=0
        for i in range(1, len(s)):
            if 65 <= ord(s[i]) <= 90:
                continue
            else:
                flag=1
                break
        if flag==0:
            l[0]=chr(ord(s[0])-32)
            for i in range(1,len(s)):
                l[i] = chr(ord(l[i]) + 32)
            print("".join(str(e) for e in l))
        else:
            print(s)
