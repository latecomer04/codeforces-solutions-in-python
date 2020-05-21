n=int(input())
mish=0
chris=0
for _ in range(n):
    l=list(map(int,input().strip().split()))
    if l[0]>l[1]:
        mish=mish+1
    elif l[1]>l[0]:
        chris=chris+1
if mish==chris:
    print("Friendship is magic!^^")
elif mish>chris:
    print("Mishka")
else:
    print("Chris")
