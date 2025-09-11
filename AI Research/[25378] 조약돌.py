N = int(input())
A = list(map(int, input().split()))

dp = [0] * N

for i in range(N):
    dp[i] = max(dp[i], dp[i - 1])
    v = A[i]
    for j in range(i + 1, N):
        v = A[j] - v
        if v == 0:
            dp[j] = max(dp[j], dp[i - 1] + 1)
            break
        elif v < 0:
            break

print(N - dp[-1])
