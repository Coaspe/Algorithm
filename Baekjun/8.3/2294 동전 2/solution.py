n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [10001] * (k + 1)
dp[0] = 0

for num in coins:
    for i in range(num, k + 1):
        dp[i] = min(dp[i], dp[i - num] + 1)

print(-1 if dp[-1] == 10001 else dp[-1])
