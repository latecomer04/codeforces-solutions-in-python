n=int(input())
s=str(n)
ref=[4,7,47,74,447,744,474,477,774,747,444,777]
a=s.count("4")
b=s.count('7')
count=a+b
if count in ref:
    print("YES")
else:
    print("NO")
