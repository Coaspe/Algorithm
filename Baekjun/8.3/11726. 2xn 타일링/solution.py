N = int(input())
dp = (1, 2)

for _ in range(N - 2):
    dp = (dp[1], (dp[0] + dp[1]) % 10007)
print(dp[1] if N != 1 else 1)
