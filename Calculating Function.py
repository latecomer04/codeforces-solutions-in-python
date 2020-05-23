n=int(input())
if n%2==0:
    a=n//2
    even=a*(1+a)
    odd=a**2
else:
    a=n//2
    odd=(a+1)**2
    even=(a)*(1+a)
print(even-odd)
