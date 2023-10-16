N = int(input())

dp = (1, 1)

for _ in range(N - 1):
    dp = (dp[1], dp[0] + dp[1])
print(dp[0])
