table=input()
hand=list(map(str,input().strip().split()))
flag=0
for i in range(len(table)):
    a=table[i]
    for j in hand:
        if j[i]==a:
            print("YES")
            flag=1
            break
    if flag==1:
        break
if flag==0:
    print("NO")
