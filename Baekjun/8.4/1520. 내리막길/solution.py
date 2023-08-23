################################################
# BFS
from collections import deque

R, C = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(R)]
dp = [[0] * (C) for _ in range(R)]

L, S = B[0][0], B[R - 1][C - 1]
candid = []
q = deque([(0, 0)])

check = [[0] * C for _ in range(R)]
check[R - 1][C - 1] = 1

while q:
    r, c = q.popleft()
    candid.append((r, c))

    for row, col in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
        if (
            0 <= row < R
            and 0 <= col < C
            and not check[row][col]
            and S < B[row][col] < L
        ):
            q.append((row, col))
            check[row][col] = 1

candid.sort(reverse=True, key=lambda x: B[x[0]][x[1]])

dp[0][0] = 1

for i, j in candid:
    for ii, jj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
        if 0 <= ii < R and 0 <= jj < C and check[ii][jj] and B[i][j] > B[ii][jj]:
            dp[ii][jj] += dp[i][j]

print(dp[-1][-1])

################################################
# DFS
import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline


def dfs(x, y):
    if d[x][y] != -1:
        return d[x][y]

    if x == n - 1 and y == m - 1:
        return 1

    d[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] < arr[x][y]:
                d[x][y] += dfs(nx, ny)

    return d[x][y]


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
d = [[-1] * m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

print(dfs(0, 0))
