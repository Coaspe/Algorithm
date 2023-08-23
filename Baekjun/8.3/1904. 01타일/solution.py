N = int(input())

if N == 1:
    print(1)
    exit(0)

dp = (1, 2)

for i in range(3, N + 1):
    dp = (dp[1], (dp[0] + dp[1]) % 15746)

print(dp[-1])
