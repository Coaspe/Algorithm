from math import sqrt

N = int(input())

MAX = 50000
dp = [MAX] * (N + 1)
dp[0] = 0

for i in range(1, N + 1):
    for j in range(1, int(sqrt(i) + 1)):
        dp[i] = min(dp[i], dp[i - j**2] + 1)

print(dp[-1])
