N = int(input())
B = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1] * N for _ in range(N)]


def dfs(r, c):
    if dp[r][c] != -1:
        return dp[r][c]

    if (r, c) == (N - 1, N - 1):
        return 1

    dp[r][c] = 0

    for row, col in (
        (r + B[r][c], c),
        (r, c + B[r][c]),
    ):
        if 0 <= row < N and 0 <= col < N:
            dp[r][c] += dfs(row, col)

    return dp[r][c]


dfs(0, 0)

print(dp[0][0])
