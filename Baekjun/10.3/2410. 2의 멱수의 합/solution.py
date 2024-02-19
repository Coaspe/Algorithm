n = int(input())
lst = [1 << i for i in range(21)]
mod = 1000000000
dp = [0] * (n + 1)
dp[0] = 1
for i in lst:
    if i <= n:
        for j in range(i, n + 1):
            dp[j] += dp[j - i]
            dp[j] %= mod
print(dp[n])
