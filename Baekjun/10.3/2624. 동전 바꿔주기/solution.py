T = int(input())
K = int(input())
PN = [[0, 0]] + [list(map(int, input().split())) for _ in range(K)]

dp = [[0 for _ in range(T + 1)] for _ in range(K + 1)]

for i in range(1, K + 1):
    for j in range(1, T + 1):
        dp[i][j] = dp[i - 1][j]
        for k in range(1, PN[i][1] + 1):
            val = k * PN[i][0]
            if j - val < 0:
                break

            if j == val:
                dp[i][j] += 1
            else:
                dp[i][j] += dp[i - 1][j - val]

print(dp[-1][-1])
