from sys import stdin
from collections import defaultdict

input = stdin.readline

N, H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
MAX = 1e9 + 7


dp = [[] for _ in range(H + 1)]
dp[1].append(MAX)

A.sort()

min_max = defaultdict(list)
min_max[1].append(1)

for i, (h, w) in enumerate(A):
    if len(min_max[h]) < 2:
        min_max[h].append(w)
        dp[h].append(MAX)
    else:
        if w < min_max[h][0]:
            min_max[h][0] = w
        elif min_max[h][1] < w:
            min_max[h][1] = w

if len(min_max[1]) > 1:
    min_max[1][0] = min_max[1][1]
    dp[1][1] = min_max[1][0] - 1
    dp[1][0] = min_max[1][0] - 1
else:
    dp[1][0] = 0

keys = sorted(min_max.keys())
max_key = 1

for j in range(1, len(keys)):
    cur = keys[j]
    prev = keys[j - 1]
    max_key = max(max_key, cur)

    dp[cur][0] = (
        min(
            abs(min_max[cur][-1] - min_max[prev][0]) + dp[prev][0],
            abs(min_max[cur][-1] - min_max[prev][-1]) + dp[prev][-1],
        )
        + (cur - prev) * 100
        + abs(min_max[cur][0] - min_max[cur][-1])
    )

    dp[cur][-1] = (
        min(
            dp[cur][-1],
            abs(min_max[cur][0] - min_max[prev][0]) + dp[prev][0],
            abs(min_max[cur][0] - min_max[prev][-1]) + dp[prev][-1],
        )
        + (cur - prev) * 100
        + abs(min_max[cur][0] - min_max[cur][-1])
    )

print(min(dp[max_key]))
