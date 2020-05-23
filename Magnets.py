n=int(input())
l=[]
m=1
for i in range(n):
    s=input()
    l.append(s)
    if i>0:
        count=1
        if l[i-1]==l[i]:
            count=count+1
        else:
            m=m+1
            count=1
print(m)




or




def get_num_groups(l):
    cur = l[0]
    numGroups = 1
    for m in l[1:]:
        if m != cur:
            cur = m
            numGroups += 1
    return numGroups


if __name__ == '__main__':
    n = int(input())
    ip = []
    for i in range(n):
        ip.append(input().strip())
    print(get_num_groups(ip))
