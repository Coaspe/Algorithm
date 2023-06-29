from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        if 2*k >= n:
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    ans += prices[i] - prices[i-1]
        
        dp = [[[0] * n] for _ in range(k+1)]

        for i in range(1, k+1):
            maxDiff = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j-1],
                               prices[j] + maxDiff)
                maxDiff = max(maxDiff, dp[i-1][j] - prices[j])

        return dp[k][n-1]
