from sys import stdin
from bisect import bisect_left

n, m = map(int, stdin.readline().strip().split())
black = list(map(int, stdin.readline().strip().split()))
black.sort()
result = 0

for i in range(m):
    a, w = map(int, stdin.readline().strip().split())
    idx = bisect_left(black, a)

    if idx == n:
        idx -= 1

    d = min(abs(black[idx] - a), abs(black[idx - 1] - a))
    result = max(result, d * w)

print(result)
