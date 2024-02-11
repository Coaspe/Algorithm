# 호텔
C, N = map(int, input().split())
hotel = [[0, 0]]

maxCost = float("INF")

for i in range(N):
    line = list(map(int, input().split()))
    hotel.append(line)

dp = [[maxCost for _ in range(C + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    cost, p = hotel[i]

    for j in range(1, C + 1):
        dp[i][j] = dp[i - 1][j]
        k = 0

        while True:
            if j - (k * p) <= 0:
                dp[i][j] = min(dp[i][j], k * cost)
                break
            else:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - k * p] + k * cost)
            k += 1

print(dp[-1][-1])
