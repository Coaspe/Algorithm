from collections import defaultdict
from bisect import bisect_left

N = int(input())
S = input()
MAX = 1000 * 1000
dp = [MAX] * N
dp[0] = 0

points = defaultdict(list)
mapping = {"B": "O", "O": "J", "J": "B"}

for i in range(N):
    points[S[i]].append(i)

for i in range(N):
    idx = bisect_left(points[mapping[S[i]]], i)
    for j in range(idx, len(points[mapping[S[i]]])):
        j = points[mapping[S[i]]][j]
        dp[j] = min(dp[j], dp[i] + (j - i) ** 2)

print(dp[-1] if dp[-1] != MAX else -1)
