N, W = map(int, input().split())

items = [tuple(map(int, input().split())) for _ in range(N)]
# dp[i][j] = 처음부터 i번째까지의 물건을 살펴보고,
# 배낭의 용량이 j였을 때 배낭에 들어간 물건의 가치합의 최댓값
dp = [[0]*(W+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, W+1):
        if j >= items[i-1][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1]
                           [j-items[i-1][0]] + items[i-1][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][W])
