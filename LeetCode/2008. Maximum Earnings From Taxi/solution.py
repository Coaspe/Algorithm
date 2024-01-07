from typing import List
from bisect import bisect_right
from collections import defaultdict


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort(key=lambda x: (x[1], x[0], x[2] + x[1] - x[0]))

        dp = [rides[0][1] - rides[0][0] + rides[0][2]] + [0] * ((N := len(rides)) - 1)

        for i in range(1, N):
            idx = bisect_right(rides, rides[i][0], key=lambda x: x[1]) - 1
            dp[i] = max(
                dp[i - 1],
                rides[i][1] - rides[i][0] + rides[i][2] + (dp[idx] if idx >= 0 else 0),
            )

        return dp[-1]


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        endAt = defaultdict(list)
        for s, e, t in rides:
            endAt[e].append((s, e - s + t))

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            for s, t in endAt[i]:
                dp[i] = max(dp[i], t + dp[s])

        return dp[-1]
