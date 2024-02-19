from typing import List
from collections import defaultdict


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        idx = 0

        for e, s, p in sorted(zip(endTime, startTime, profit)):
            endTime[idx] = e
            startTime[idx] = s
            profit[idx] = p
            idx += 1

        dp = [profit[0]] + [0] * ((n := len(profit)) - 1)

        for i in range(1, n):
            idx = bisect_right(endTime, startTime[i]) - 1
            dp[i] = max(dp[i - 1], profit[i] + dp[idx] * int(idx >= 0))

        return dp[-1]
