# BOJ 2468. 안전 영역

import sys

sys.setrecursionlimit(100000)


def dfs(x, y, h):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if graph[x][y] > h and not visited[x][y]:
        visited[x][y] = True
        dfs(x - 1, y, h)
        dfs(x + 1, y, h)
        dfs(x, y - 1, h)
        dfs(x, y + 1, h)
        return True
    return False


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
max_height = max(map(max, graph))
max_count = 0
for h in range(max_height):
    visited = [[False] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            count += int(dfs(i, j, h))
    max_count = max(max_count, count)
print(max_count)
