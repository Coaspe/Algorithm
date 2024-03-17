from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # 4 방향 중 현재 위치보다 큰 것 중에 가장 작은 순서대로 탐색
        R, C = len(matrix), len(matrix[0])
        dp = [[1] * C for _ in range(R)]
        D = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if dp[r][c] > 1:
                return dp[r][c]

            max_val = 0
            for dx, dy in D:
                row, col = r + dx, c + dy

                if 0 <= row < R and 0 <= col < C and matrix[r][c] < matrix[row][col]:
                    max_val = max(max_val, dfs(row, col))

            dp[r][c] += max_val

            return dp[r][c]

        ans = 0
        for r in range(R):
            for c in range(C):
                if dp[r][c] == 1:
                    dfs(r, c)
                ans = max(ans, dp[r][c])
        return ans
