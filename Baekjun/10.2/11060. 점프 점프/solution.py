N = int(input())
A = list(map(int, input().split()))
MAX = 1000
dp = [MAX] * (N)
dp[0] = 0

for i in range(N):
    for j in range(A[i], 0, -1):
        if i + j < N:
            dp[j + i] = min(dp[j + i], dp[i] + 1)
print(dp[-1] if dp[-1] != MAX else -1)
