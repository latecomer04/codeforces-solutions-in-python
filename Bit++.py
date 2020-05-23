n=int(input())
x=0
for i in range(n):
    s=input()
    a=s.count("+")
    if a>1:
        x=x+1
    else:
        x=x-1
print(x)
