N = int(input())

forest = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1] * N for _ in range(N)]
ans = 0


def dfs(r, c, pr, pc, val):
    if dp[r][c] >= 0:
        return dp[r][c]

    max_val = 1

    for row, col in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
        if (
            0 <= row < N
            and 0 <= col < N
            and (pr, pc) != (row, col)
            and forest[row][col] > forest[r][c]
        ):
            max_val = max(max_val, dfs(row, col, r, c, val + 1) + 1)

    dp[r][c] = max_val

    global ans
    ans = max(ans, dp[r][c])

    return dp[r][c]


for r in range(N):
    for c in range(N):
        if dp[r][c] == -1:
            dfs(r, c, -1, -1, 1)

print(ans)
