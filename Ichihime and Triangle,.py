#basic logic is sum of two sides must be greater than third one as it is guaranteed in the ques the ans exists then the sum of max possible sides 
must be greater than the third side of min len(ie that is equal to len of 2nd side here)...or it was veery intutive that u cant use loops here...
u must have some straight forward logic

t=int(input())
for  i in range(t):
    l=list(map(int,input().strip().split()))
    a=l[1]
    b=l[2]
    c=l[3]
    print(a,end=" ")
    print(b,end=" ")
    print(b,end=" ")
    print()
