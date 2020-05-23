n=int(input())
dict={}
for i in range(n):
    s=input()
    if s not in dict:
        dict[s]=1
        print("OK")
    else:
        a=dict[s]
        dict[s]=a+1
        print(s+str(a))
