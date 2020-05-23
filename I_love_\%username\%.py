def func(n,l):
    count = 0
    for i in range(1, n):
            c=l[:i]
            a=max(c)
            b=min(c)
            if l[i] > a :
                count=count+1
            if l[i]< b:
                count=count+1
    return (count)

if __name__=="__main__":
    n = int(input())
    l = list(map(int, input().strip().split()))
    print(func(n,l))
