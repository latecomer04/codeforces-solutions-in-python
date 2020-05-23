s1=list(map(int,input().strip().split()))
s2=list(map(int,input().strip().split()))
s3=list(map(int,input().strip().split()))
s4=list(map(int,input().strip().split()))
s5=list(map(int,input().strip().split()))

l=[]
l.append(s1)
l.append(s2)
l.append(s3)
l.append(s4)
l.append(s5)

for i in range(5):
    count=0
    a=l[i]
    if 1 in a:
        b=a.index(1)
        count=count+(abs(2-b))+(abs(2-i))
        print(count)
        break
