MOD = 998244353

dp = [[0] * 1000010 for _ in range(2)]

n, m = map(int, input().split())

dp[1][1] = m

for i in range(1, n):
    dp[0][i+1] += dp[0][i] * (m-2)
    dp[1][i+1] += dp[0][i]
    dp[0][i+1] += dp[1][i] * (m-1)
    dp[0][i+1] %= MOD
    dp[1][i+1] %= MOD

print(dp[0][n])
