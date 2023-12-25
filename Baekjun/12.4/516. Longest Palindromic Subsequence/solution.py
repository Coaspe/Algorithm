class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        dp = [[0] * N for _ in range(N)]

        for i in range(N):
            dp[i][i] = 1
            for j in range(i - 1, -1, -1):
                if s[i] == s[j]:
                    dp[j][i] = 2 + dp[j + 1][i - 1]
                else:
                    dp[j][i] = max(dp[j + 1][i], dp[j][i - 1])

        return dp[0][N - 1]
