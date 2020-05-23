n=int(input())
s=input()
l=list(s)
for i in range(n):
    if 65<=ord(l[i])<=90:
        l[i]=chr(ord(l[i])+32)
a=set(l)
if len(a)>=26:
    print('YES')
else:
    print("NO")
