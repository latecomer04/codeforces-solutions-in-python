y=int(input())
s=str(y+1)
a=s[0]
b=s[1]
c=s[2]
d=s[3]
if s.count(a) == 1 and s.count(b) == 1 and s.count(c) == 1 and s.count(d) == 1:
    print(y+1)
else:
    for i in range(10**4):
        y=y+1
        s=str(y)
        a = s[0]
        b = s[1]
        c = s[2]
        d = s[3]

        if s.count(a) == 1 and s.count(b) == 1 and s.count(c) == 1 and s.count(d) == 1:
            print(y)
            break
