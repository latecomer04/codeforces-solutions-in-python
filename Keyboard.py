n=input()
s=input()
l=list(s)
a="qwertyuiopasdfghjkl;zxcvbnm,./"
if n=="R":
    for i in range(len(s)):
        m=l[i]
        b=a.index(m)
        p=a[b-1]
        l[i]=p
else:
    for i in range(len(s)):
        m=l[i]
        b=a.index(m)
        p=a[b+1]
        l[i]=p
print("".join(str(e) for e in l))
