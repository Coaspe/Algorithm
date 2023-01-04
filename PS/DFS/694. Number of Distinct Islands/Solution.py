# https://leetcode.com/problems/number-of-distinct-islands/description/
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        distinct = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c, indice: str):
            grid[r][c] = 0
            for idx, p in enumerate([(r, c-1), (r-1, c), (r, c+1), (r+1, c)]):
                if 0 <= p[0] <= rows-1 and 0 <= p[1] <= cols-1 and grid[p[0]][p[1]]:
                    indice += dfs(p[0], p[1], str(idx))

            indice += '0'
            return indice

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    distinct.add(dfs(i, j, "-1"))

        return len(distinct)
