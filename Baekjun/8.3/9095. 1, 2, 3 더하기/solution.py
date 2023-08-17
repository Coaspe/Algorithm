T = int(input())
pro = [int(input()) for _ in range(T)]
max_val = max(pro) + 1
dp = [0] * max_val
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, max_val):
    dp[i] += dp[i - 3]
    dp[i] += dp[i - 2]
    dp[i] += dp[i - 1]

for i in pro:
    print(dp[i])
