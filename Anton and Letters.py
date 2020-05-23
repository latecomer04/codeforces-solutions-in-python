s=input()
l=[]
for i in s:
    if 97<=ord(i)<=122:
        if i not in l:
            l.append(i)
print(len(l))
