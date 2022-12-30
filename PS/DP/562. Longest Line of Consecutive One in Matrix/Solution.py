class Solution:
    # row col dig1 dig2
    def longestLine(self, mat: List[List[int]]) -> int:
        len_r, len_c = len(mat), len(mat[0])
        dp = [[[0, 0, 0, 0]] * len_c for _ in range(len_r)]
        self.answer = max(0, mat[0][0])
        for i in range(len_r):
            for j in range(len_c):
                if not mat[i][j]:
                    continue
                dp[i][j] = [1, 1, 1, 1]
                for idx, p in enumerate([(i, j-1), (i-1, j), (i-1, j-1), (i-1, j+1)]):
                    if 0 <= p[0] <= len_r-1 and 0 <= p[1] <= len_c-1:
                        dp[i][j][idx] += dp[p[0]][p[1]][idx]
                    self.answer = max(self.answer, dp[i][j][idx])
        return self.answer
