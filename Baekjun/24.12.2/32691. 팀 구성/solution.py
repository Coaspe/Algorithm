N, K = map(int, input().split())

dp = [0] * (N)


V = [list(map(int, input().split()))[::-1] for _ in range(N)]
V.sort()

for i in range(2, N):
    for a in range(2, min(i + 1, 5)):
        if V[i][0] - V[i - a][0] > K:
            break

        for b in range(1, a):
            acc = V[i][1] + V[i - a][1] + V[i - b][1]
            dp[i] = max(dp[i - 1], dp[i - a - 1] + acc)

print(dp[-1])
