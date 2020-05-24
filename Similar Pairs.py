t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().strip().split()))
    even=0
    odd=0
    flag=0
    for i in l:
        if i%2==0:
            even+=1
        else:
            odd+=1
    if even%2!=odd%2:
        print("no")
    else:
        if even%2==0:
            print("yes")
        else:
            for i in range(n-1):
                for j in range(i+1,n):
                    if abs(l[i]-l[j])==1 and l[i]%2!=l[j]%2:
                        print("yes")
                        flag=1
                        break
                if flag==1:
                    break
            if flag==0:
                print("no")
