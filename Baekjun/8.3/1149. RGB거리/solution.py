N = int(input())
dp = [[0] * 3 for _ in range(N)]

a, b, c = map(int, input().split())

dp[0][0] = a
dp[0][1] = b
dp[0][2] = c

for i in range(1, N):
    a, b, c = map(int, input().split())
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + a
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + b
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + c

print(min(dp[-1]))
