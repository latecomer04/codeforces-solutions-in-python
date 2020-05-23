s=input()
t=input()

j=""
for i in range(len(s)):
    if s[i]==t[i]:
        j=j+"0"
    else:
        j=j+"1"
print(j)
