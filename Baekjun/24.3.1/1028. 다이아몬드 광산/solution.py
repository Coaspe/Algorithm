from sys import stdin

input = stdin.readline
R, C = map(int, input().split())
mine = [input() for _ in range(R)]

# dp[i][j][k] = (i, j)로 내려오는 누적합 (k는 각 방향)

# 왼-오, 오-왼
dp = [[[0, 0]] * C for _ in range(R)]
candid = range(2, min(R // 2 + 1, C // 2 + 1) + 1)
ans = 0

for r in range(R):
    for c in range(C):
        if mine[r][c] == "1":
            dp[r][c] = [1, 1]
            ans = 1


def prefix_sum(r, c, d):
    if mine[r][c] == "0":
        return

    if d == 0:
        if r - 1 >= 0 and c - 1 >= 0:
            dp[r][c][0] += dp[r - 1][c - 1][0]
        if r + 1 < R and c + 1 < C:
            prefix_sum(r + 1, c + 1, d)
    else:
        if r - 1 >= 0 and c + 1 < C:
            dp[r][c][1] += dp[r - 1][c + 1][1]
        if r + 1 < R and c - 1 >= 0:
            prefix_sum(r + 1, c - 1, d)


for r in range(R):
    for c in range(C):
        if mine[r][c] == "1":
            if dp[r][c][0] == 1:
                prefix_sum(r, c, 0)
            if dp[r][c][1] == 1:
                prefix_sum(r, c, 1)

for r in range(R):
    for c in range(C):
        min_value = min(dp[r][c])

        if min_value < ans:
            continue

        for k in range(min_value, 0, -1):
            if (
                r - k + 1 >= 0
                and c - (k - 1) >= 0
                and c + k - 1 < C
                and dp[r - k + 1][c - (k - 1)][1] >= k
                and dp[r - k + 1][c + k - 1][0] >= k
            ):
                ans = max(ans, k)
                break
print(ans)
