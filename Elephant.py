n=int(input())
if n<=5:
    print(1)
else:
    for i in range(2,10**8):
        if 5*i>=n:
            print(i)
            break
        else:
            continue
