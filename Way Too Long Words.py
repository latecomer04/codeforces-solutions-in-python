n=int(input())
for i in range(n):
    s=input()
    if len(s)>10:
        b = len(s) - 2
        result = s[0] + str(b) + s[-1]
        print(result)
    else:
        print(s)
