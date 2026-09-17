import math
a = float(input())
b = float(input())
r = min(a,b)
R = max(a,b)
print(math.pi * (R*R - r*r))
