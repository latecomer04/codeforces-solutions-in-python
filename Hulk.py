n=int(input())
if n==1:
    print("I hate it")
else:
    s=""
    if n%2==0:
        for i in range(n-1):
            if i%2==0:
                if i==0:
                    s=s+"I hate that"
                else:
                    s=s+" I hate that"
            else:
                s=s+" I love that"
        s=s+" I love it"
    else:
        for i in range(n-1):
            if i%2==0:
                if i==0:
                    s=s+"I hate that"
                else:
                    s = s + " I hate that"
            else:
                s=s+" I love that"
        s=s+" I hate it"
    print(s)
