n = int(input())
p = list(map(float, input().split()))
dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(1, n + 1):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i - 1][j] * (1 - p[i - 1])
        else:
            dp[i][j] = dp[i - 1][j] * (1 - p[i - 1]) + dp[i - 1][j - 1] * p[i - 1]
ans = 0
for j in range((n + 1) // 2, n + 1):
    ans += dp[-1][j]
print(ans)
