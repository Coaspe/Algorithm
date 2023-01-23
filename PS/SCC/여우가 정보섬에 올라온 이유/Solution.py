import collections
import bisect

N = int(input())

points = collections.defaultdict(list)
for _ in range(N):
    a, b = map(int, input())
    bisect.bisect_left(points[a], b)
    pass
