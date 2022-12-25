from typing import List


class Solution:
    l1, r1, t1, b1 = float('inf'), 0, float('inf'), 0

    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        visitied = set(), set()
        m, n = len(image), len(image[0])

        def dfs(r, c):
            visitied.add((r, c))

            self.l1, self.r1, self.t1, self.b1 = \
                min(self.l1, c), max(self.r1, c), min(
                    self.t1, r), max(self.b1, r)

            for row, col in [(r+1, c), (r, c+1), (r-1, c), (r, c-1)]:
                if 0 <= row <= m - 1 and 0 <= col <= n - 1 and \
                        image[row][col] == "1" and (row, col) not in visitied:
                    dfs(row, col)

        dfs(x, y)

        return (abs(self.l1-self.r1)+1) * (abs(self.t1-self.b1)+1)
