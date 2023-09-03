import math
N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

ans = math.inf

for i in range(3):
    dp = [[math.inf] * 3 for _ in range(N)]
    dp[0][i] = cost[0][i]
    for m in range(1, N):
        for j in range(3):
            dp[m][j] = min(dp[m-1][k] for k in range(3) if k != j) + cost[m][j]
    for j in range(3):
        if i != j:
            ans = min(ans, dp[N-1][j])
print(ans)
