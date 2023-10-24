import sys

input = sys.stdin.readline
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

MAX = 1000 * 100 + 1
dp = [[[MAX] * 3 for _ in range(M)] for _ in range(N)]

for i in range(M):
    for k in range(3):
        dp[0][i][k] = A[0][i]


def cal(v, j):
    min_v = max(v)
    for i in range(3):
        if v[i] != MAX and i != j:
            min_v = min(min_v, v[i])
    return min_v


for i in range(1, N):
    for j in range(M):
        # 0 left down, 1 down, 2 right down
        dp[i][j][0] = cal(dp[i - 1][j], 0) + A[i][j]

        if j + 1 < M:
            dp[i][j][1] = cal(dp[i - 1][j + 1], 1) + A[i][j]
        if j - 1 >= 0:
            dp[i][j][2] = cal(dp[i - 1][j - 1], 2) + A[i][j]

ans = MAX

for i in dp[-1]:
    ans = min(ans, min(i))

print(ans)
