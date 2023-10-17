N = int(input())
A = [0] + list(map(int, input().split()))
MAX = 4999 * 1000000 + 1
dp = [MAX] * (N + 1)
dp[1] = 0
for i in range(1, N):
    for j in range(i + 1, N + 1):
        dp[j] = min(dp[j], max((j - i) * (1 + abs(A[i] - A[j])), dp[i]))
print(dp[-1])
