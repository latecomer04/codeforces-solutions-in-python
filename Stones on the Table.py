n=int(input())
s=input()
count=0
z=s[0]
for i in range(1,n):
    if z==s[i]:
        count=count+1
    z=s[i]

print(count)
