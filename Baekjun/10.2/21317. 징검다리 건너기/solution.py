N = int(input())
J = [list(map(int, input().split())) for _ in range(N - 1)]
K = int(input())
MAX = 5000 * 20
dp = [[MAX] * 2 for _ in range(N)]
dp[0] = [0, 0]

for i in range(N - 1):
    if 1 + i < N:
        dp[i + 1][0] = min(dp[i + 1][0], dp[i][0] + J[i][0])
        dp[i + 1][1] = min(dp[i + 1][1], dp[i][1] + J[i][0])
    if 2 + i < N:
        dp[i + 2][0] = min(dp[i + 2][0], dp[i][0] + J[i][1])
        dp[i + 2][1] = min(dp[i + 2][1], dp[i][1] + J[i][1])
    if 3 + i < N:
        dp[i + 3][1] = min(dp[i + 3][1], dp[i][0] + K)

print(min(dp[-1]))
