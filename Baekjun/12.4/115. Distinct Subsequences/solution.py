class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        NS, NT = len(s), len(t)

        # dp[i][j] = s[0:i)에 존재하는 유일한 t[0:j)의 수
        dp = [[0] * (NT + 1) for _ in range(NS + 1)]

        for i in range(NS + 1):
            dp[i][0] = 1

        for i in range(1, NS + 1):
            for j in range(1, NT + 1):
                dp[i][j] = dp[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[-1][-1]
