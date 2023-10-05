import sys

sys.setrecursionlimit(250001)
input = sys.stdin.readline
N, M = map(int, input().split())
B = [input() for _ in range(N)]

dp = [[-1] * M for _ in range(N)]
v = [[0] * M for _ in range(N)]
m = {
    "U": lambda x, y: (x - 1, y),
    "R": lambda x, y: (x, y + 1),
    "D": lambda x, y: (x + 1, y),
    "L": lambda x, y: (x, y - 1),
}

ans = 0


def dfs(r, c):
    if dp[r][c] != -1:
        return dp[r][c]

    row, col = m[B[r][c]](r, c)

    if row < 0 or col < 0 or N <= row or M <= col:
        dp[r][c] = 1
    elif v[row][col]:
        dp[r][c] = 0
    else:
        v[row][col] = 1
        dp[r][c] = dfs(row, col)
        v[row][col] = 0

    global ans
    ans += dp[r][c]

    return dp[r][c]


for r in range(N):
    for c in range(M):
        if dp[r][c] == -1:
            v[r][c] = 1
            dfs(r, c)
            v[r][c] = 0
print(ans)
