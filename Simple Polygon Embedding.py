import math
t=int(input())
for _ in range(t):
    n=int(input())
    z=2*n
    a = (math.cos(math.pi / z))             #these formulas comes from the derivation of apothem and radius of any regular polygon
    b = (math.sin(math.pi / z))
    print(a / b)
