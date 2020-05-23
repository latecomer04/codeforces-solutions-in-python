s=input()
l=list(s)
arr=["A","O","Y","E","U","I","a","o","y","e","u","i"]
for i in range(len(s)):
    var=l[i]
    if var in arr:
        l[i]="-"

for i in range(len(l)):
    a=l[i]
    if 65<=ord(a)<=90:
        l[i]=chr(ord(a)+32)
b=[]
for i in l:
    if i=="-":
        continue
    else:
        b.append(i)
list=[]
for i in range(2*len(b)):
    if i%2==0:
        list.append(".")
    else:
        list.append(b[(i-1)//2])

print("".join(str(e) for e in list))
