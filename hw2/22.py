import math
n, k, m = map(int, input().split())
a = math.ceil((n * 2) / k)
print(a * m)
