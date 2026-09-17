import math
a = float(input())
b = float(input())
c = float(input())
cosa = math.degrees(math.acos((b**2 + c**2 - a**2) / (2*b*c)))
cosb = math.degrees(math.acos((a**2 + c**2 - b**2) / (2*a*c)))
cosc = math.degrees(math.acos((a**2 + b**2 - c**2) / (2*a*b)))
print(cosa, cosb, cosc, sep='\n')
