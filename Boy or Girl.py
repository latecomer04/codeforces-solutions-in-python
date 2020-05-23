s=input()
l=[]
for i in s:
    if i in l:
        continue
    else:
        l.append(i)
if (len(l))%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
