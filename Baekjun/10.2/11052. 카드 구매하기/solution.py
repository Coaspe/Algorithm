N = int(input())
A = list(map(int, input().split()))
dp = [0] * (N + 1)
dp[1] = A[0]

for i in range(2, N + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i - j] + A[j - 1], dp[i])
print(dp[-1])
