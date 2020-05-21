t=int(input())
for i in range(t):
    a=int(input())
    if 360*(180-a)==0:    #using formula 180*(n-2)=sum of all angles as it is regular polygon so divide by n(the no of sides)
        print("YES")      # (180/n)*(n-2)=a  ie(angle) and we know ie no of sides must be integer on simplifing it we will get the same eqn
    else:
        print("NO")
