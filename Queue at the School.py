l=list(map(int,input().strip().split()))
n=l[0]
k=l[1]
s=input()
arr=list(s)
for j in range(k):
    i=0
    while i<n:
        if arr[i]=="G":
            i=i+1
            continue
        else:
            if i < n -1:
                if arr[i] == "B" and arr[i + 1] == "G":
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    i = i + 2
                else:
                    i=i+1
            else:
                i=i+1


print("".join(str(e) for e in arr))
