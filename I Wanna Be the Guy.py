def name():
    n=int(input())
    l=list(map(int,input().strip().split()))
    arr=list(map(int,input().strip().split()))
    l.pop(0)
    arr.pop(0)
    for i in range(1,n+1):
        if i not in l and i not in arr:
            return "Oh, my keyboard!"
    return "I become the guy."

print(name())
