from typing import List
from math import inf
from functools import cache

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @cache
        def dp(i, j):
            if i == 0 and j == 0: return (grid[0][0], grid[0][0])
            if i < 0 or j < 0: return (-inf, inf)

            if grid[i][j] == 0: return (0, 0)

            mx1, mn1 = dp(i-1, j) # from top
            mx2, mn2 = dp(i, j-1) # from left

            mx, mn = max(mx1, mx2) * grid[i][j], min(mn1, mn2) * grid[i][j]

            return (mx, mn) if grid[i][j] > 0 else (mn, mx)
        
        mx, _ = dp(m-1, n-1)

        return -1 if mx<0 else mx % (1e9+7)