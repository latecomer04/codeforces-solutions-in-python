l=list(map(int,input().strip().split()))
s=input()
one=s.count("1")
two=s.count("2")
three=s.count("3")
four=s.count("4")
ans=one*l[0]+two*l[1]+three*l[2]+four*l[3]
print(ans)
