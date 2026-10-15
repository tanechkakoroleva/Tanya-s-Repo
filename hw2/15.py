n, k, m = map(int, input().split())
dist1 = abs(k - m)
dist2 = n - dist1
min_dist = min(dist1, dist2)
if min_dist == 0:
    print(0)
else:
    print(min_dist - 1)
