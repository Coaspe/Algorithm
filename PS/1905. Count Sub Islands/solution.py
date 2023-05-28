from typing import List


class Solution:
    answer = 0

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        len_row, len_col = len(grid1), len(grid1[0])
        visited = [[0]*len_col for _ in range(len_row)]

        def is_safe(r, c):
            return 0 <= r and r <= len_row - 1 and 0 <= c and c <= len_col - 1

        def dfs(r, c, flag):
            visited[r][c] = 1
            for row, col in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                if not is_safe(r+row, c+col) or visited[r+row][c+col] or not grid2[r+row][c+col]:
                    continue
                if not grid1[r+row][c+col] and flag:
                    flag = False
                    self.answer -= 1
                flag = dfs(r+row, c+col, flag)
            return flag

        for r in range(len_row):
            for c in range(len_col):
                if visited[r][c] or not grid2[r][c] or not grid1[r][c]:
                    continue
                self.answer += 1
                dfs(r, c, True)

        return self.answer
