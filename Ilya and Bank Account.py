n=int(input())

if n<0:
    s=str(n)
    l=list(s)
    if l[-1]>l[-2]:
        l.pop(-1)
        if len(l)==2 and l[1]==0:
            l.pop(0)
    else:
        l.pop(-2)
        if len(l)==2 and l[1]=="0":
            l.pop(0)
    print("".join(str(e) for e in l))
else:
    print(n)
