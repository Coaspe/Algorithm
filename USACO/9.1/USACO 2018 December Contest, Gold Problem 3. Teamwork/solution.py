N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

first_max = max(A[:K])
dp = [0] * N

mx = A[0]
dp[0] = mx

for k in range(1, K):
    mx = max(mx, A[k])
    dp[k] = mx * (k + 1)

for i in range(K, N):
    mx = A[i]
    for k in range(K):
        mx = max(mx, A[i - k])
        dp[i] = max(dp[i], dp[i - k - 1] + (k + 1) * mx)

print(dp[-1])
