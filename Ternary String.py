t=int(input())
for _ in range(t):
    s=input()
    n=len(s)
    if s.count("3")==0 or s.count("1")==0 or s.count("2")==0:
        print(0)
    else:
        m=10**15
        for i in range(0,n-2):
            a=s[i]
            b=s[i+1]
            if a!=b:
                for j in range(i+2,n):
                    if s[j]!=a and s[j]!=b:
                        m=min(m,j-i+1)
        if m==10**15:
            print(0)
        else:
            print(m)
