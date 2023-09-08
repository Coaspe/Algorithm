class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        # dp[length][i][j] => s1의 i 인덱스, s2의 j 인덱스 부터 length 길이의 문자열이 서로 scrambled 문자인지 여부를 나타낸다.
        dp = [[[False for _ in range(n)] for _ in range(n)] for _ in range(n + 1)]

        for i in range(n):
            for j in range(n):
                dp[1][i][j] = s1[i] == s2[j]

        for length in range(2, n + 1):
            for i in range(n + 1 - length):
                for j in range(n + 1 - length):
                    for new_length in range(1, length):
                        # s1
                        dp1 = dp[new_length][i]
                        # s2
                        dp2 = dp[length - new_length][i + new_length]

                        dp[length][i][j] |= dp1[j] and dp2[j + new_length]
                        dp[length][i][j] |= dp1[j + length - new_length] and dp2[j]

        return dp[n][0][0]
