N, K = map(int, input().split())

dp = [0] * (N)


V = [list(map(int, input().split()))[::-1] for _ in range(N)]
V.sort()
# 원하는 등수, 실력

ans = 0
for i in range(2, N):
    dp[i] = dp[i - 1]
    for j in range(2, min(i + 1, 5)):
        if V[i][0] - V[i - j][0] > K:
            break

        for k in range(i - j + 1, i):
            dp[i] = max(dp[i], dp[i - j - 1] + V[i][1] + V[i - j][1] + V[k][1])
