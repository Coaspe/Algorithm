import math

N, W = map(int, input().split())

items = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(N)]

sum_v = sum(v for _, v in items)
# dp[i][j] = i번째 물건까지 볼 때, j의 가치를 만들 수 있는 무게 합의 최소값.
dp = [[math.inf] * (sum_v + 1) for _ in range(N + 1)]
dp[0][0] = 0

ans = 0
for i in range(1, N + 1):
    for j in range(sum_v + 1):
        dp[i][j] = min(dp[i - 1][j], dp[i][j])

        if j - items[i][1] >= 0:
            dp[i][j] = min(dp[i][j], dp[i - 1][j - items[i][1]] + items[i][0])

        if dp[i][j] <= W:
            ans = max(ans, j)
print(ans)
