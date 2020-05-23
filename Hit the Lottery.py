n=int(input())
l=[100,20,10,5,1]
count=0
if n>=100:
        if n%100==0:
            count=count+n//100
            n=n-100*(n//100)
        else:
            a=n//100
            n=n-100*a
            count=count+a
if n>=20:
        if n%20==0:
            count=count+n//20
            n=n-20*(n//20)
        else:
            count = count + n // 20
            n=n-20*(n//20)

if n>=10:
        if n%10==0:
            count=count+n//10
            n=n-10*(n//10)
        else:
            count = count + n // 10
            n=n-10* (n//10)

if n>=5:
        if n%5==0:
            count=count+n//5
            n=n-5* (n//5)
        else:
            count = count + n // 5
            n=n-5* (n//5)

if n>=1:
        count=count+n//1
print(count)
