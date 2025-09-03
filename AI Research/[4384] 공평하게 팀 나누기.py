N = int(input())
K = [int(input()) for _ in range(N)]
max_val = max(K) * (N // 2)
dp = [[0] * (max_val + 1) for _ in range(N + 1)]

dp[0][0] = 1

for i in range(N):
    for j in range(N // 2, 0, -1):
        for k in range(max_val, K[i] - 1, -1):
            dp[j][k] |= dp[j - 1][k - K[i]]

T = sum(K)
ans = (0, T)
for k in range(max_val + 1):
    if dp[N // 2][k]:
        ans = min(ans, (k, T - k), key=lambda x: abs(x[0] - x[1]))

print(*sorted(ans))
