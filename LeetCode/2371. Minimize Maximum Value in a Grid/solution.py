from typing import List


class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        aux = sorted([(grid[i][j], i, j) for j in range(n) for i in range(m)])

        row_mins, col_mins = [0] * m, [0] * n

        for _, i, j in aux:
            grid[i][j] = max(row_mins[i], col_mins[j]) + 1

            row_mins[i] = max(row_mins[i], grid[i][j])
            col_mins[j] = max(col_mins[j], grid[i][j])

        return grid
