n=int(input())
count=0
ini=0
p=0
for i in range(10**5):
    count=count+5*2**i
    if count<n:
        continue
    else:
        p=i
        if i>0:
            ini=count=count-5*2**i
        break

if n<=5:
    l=["Sheldon","Leonard","Penny","Rajesh","Howard"]
    print(l[n-1])
else:
    n = n - ini
    i = 0
    while n >= 0:
        n = n - 2 ** p
        i = i + 1
    if i==1:
        print("Sheldon")
    elif i==2:
        print("Leonard")
    elif i==3:
        print("Penny")
    elif i==4:
        print("Rajesh")
    elif i==5:
        print("Howard")
