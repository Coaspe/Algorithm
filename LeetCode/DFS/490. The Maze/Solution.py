from typing import List, Tuple


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = set((start[0], start[1]))
        rows, cols = len(maze), len(maze[0])

        def find_nearst_wall(p: Tuple[int, int], idx) -> Tuple[int, int]:
            if idx == 0:
                while p[0] >= 0 and maze[p[0]][p[1]] == 0:
                    p = (p[0]-1, p[1])
                p = (p[0]+1, p[1])
            if idx == 1:
                while p[0] <= rows-1 and maze[p[0]][p[1]] == 0:
                    p = (p[0]+1, p[1])
                p = (p[0]-1, p[1])
            elif idx == 2:
                while p[1] <= cols-1 and maze[p[0]][p[1]] == 0:
                    p = (p[0], p[1]+1)
                p = (p[0], p[1] - 1)
            elif idx == 3:
                while p[1] >= 0 and maze[p[0]][p[1]] == 0:
                    p = (p[0], p[1]-1)
                p = (p[0], p[1] + 1)

            return p

        def dfs(cell):
            if cell == tuple(destination):
                return True
            ret = False

            for i in range(4):
                if not ret:
                    nearst = find_nearst_wall(cell, i)
                    if nearst not in visited:
                        # No need to remove visited cell.
                        visited.add(nearst)
                        ret = ret or dfs(nearst)
                else:
                    return ret
            return ret

        return dfs(tuple(start))


def hasPath(maze, start, destination):
    m, n, seen = len(maze), len(maze[0]), set()

    def dfs(i, j):
        if [i, j] == destination:
            return True
        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            x, y = i, j
            while 0 <= x+dx < m and 0 <= y+dy < n and not maze[x+dx][y+dy]:
                x, y = x+dx, y+dy
            if (x, y) not in seen:
                seen.add((x, y))
                if dfs(x, y):
                    return True
        return False
    return dfs(*start)
