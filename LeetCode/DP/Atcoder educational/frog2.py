import math
N, K = map(int, input().split())
h = list(map(int, input().split()))
INF = math.inf
dp = [INF]*len(h)

dp[0], dp[1] = 0, abs(h[1]-h[0])

for i in range(2, N):
    for j in range(K, 0, -1):
        dp[i] = min(dp[i], dp[i-j] + abs(h[i]-h[i-j]))

print(dp[N-1])
