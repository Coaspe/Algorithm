T = int(input())
dp = [[0] * 4 for _ in range(100001)]
MOD = 1e9 + 9
dp[1][1] = 1
dp[2][2] = 1
dp[3] = [0, 1, 1, 1]

for i in range(4, 100001):
    for j in range(1, 4):
        for k in range(1, 4):
            if j != k:
                dp[i][j] += dp[i - j][k]
                dp[i][j] %= MOD
while T:
    T -= 1
    print(int(sum(dp[int(input())]) % MOD))
