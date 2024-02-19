N = int(input())
dp = (0, 1)
MOD = 1_000_000_000
for i in range(3, N + 1):
    dp = (dp[1], (dp[0] + dp[1]) * (i - 1) % MOD)
print(dp[1] if N != 1 else dp[0])
