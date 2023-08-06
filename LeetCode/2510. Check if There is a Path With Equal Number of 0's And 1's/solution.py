from functools import cache
from typing import Literal


class Solution:
    def isThereAPath(self, grid: list[list[int]]) -> bool:
        def remap(x: int, y: int) -> Literal[-1, 1]:
            return (-1, 1)[grid[x][y]]

        @cache
        def dp(i: int, j: int, net: int = 0) -> bool:
            net += remap(i, j)
            if (i, j) == (0, 0):
                return net == 0
            return (i > 0 and dp(i - 1, j, net)) or (j > 0 and dp(i, j - 1, net))

        return dp(len(grid) - 1, len(grid[0]) - 1)
