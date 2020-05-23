l = list(map(int, input().strip().split()))
k=l[0]
r=l[1]
for i in range(1,10**9):
    a=k*i
    if a%10==0:
        print(i)
        break
    elif a%10==r:
        print(i)
        break
