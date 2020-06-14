n=int(input())
s=input()
one=0
zero=0
one=one+s.count("n")
zero=zero+s.count("z")
for i in range(one):
    print("1",end=" ")
for i in range(zero):
    print("0",end=" ")
