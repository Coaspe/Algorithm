import sys

mod = 1e9+3
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = 1
    dp[i][1] = i

for i in range(2, k + 1):
    for j in range(2*i, n + 1):
        if j == 2*i:
            dp[j][i] = 2
        else:
            dp[j][i] = (dp[j-1][i] + dp[j-2][i-1]) % mod

print(int(dp[n][k]))
