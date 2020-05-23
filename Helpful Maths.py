s=input()

l=[]
for i in s:
    if i=="+":
        continue
    else:
        l.append(i)
l.sort()
k=[]
for i in range(2*(len(l))-1):
    if i%2==0:
        k.append(l[i//2])
    else:
        k.append("+")
print("".join(str(e) for e in k))
