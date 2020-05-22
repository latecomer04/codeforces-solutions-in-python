l=list(map(int,input().strip().split()))
row=l[0]
col=l[1]
flag=0
for i in range(row):
    arr=list(map(str,input().strip().split()))
    if "C" in arr or "M" in arr or "Y" in arr:
        print("#Color" )
        flag=1
        break
if flag==0:
    print("#Black&White")
