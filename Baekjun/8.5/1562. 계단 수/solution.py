N = int(input())
dp = [[[0 for _ in range(1 << 10)] for _ in range(10)] for _ in range(N + 1)]

for i in range(10):
    dp[1][i][1 << i] = 1

for i in range(2, N + 1):
    for j in range(10):
        for k in range(1 << 10):
            if j == 0:
                dp[i][j][(1 << j) | k] += dp[i - 1][j + 1][k]
            elif j == 9:
                dp[i][j][(1 << j) | k] += dp[i - 1][j - 1][k]
            else:
                dp[i][j][(1 << j) | k] += dp[i - 1][j + 1][k]
                dp[i][j][(1 << j) | k] += dp[i - 1][j - 1][k]

ans = 0
max = (1 << 10) - 1

for i in range(1, 10):
    ans += dp[N][i][max]
    ans %= 1_000_000_000

print(ans)
