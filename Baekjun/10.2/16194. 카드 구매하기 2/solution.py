N = int(input())
A = [0] + list(map(int, input().split()))

dp = [A[i] for i in range(N + 1)]

for i in range(2, N + 1):
    for j in range(1, i + 1):
        dp[i] = min(dp[i], dp[i - j] + A[j])
print(dp[-1])
