N = int(input())
A = list(map(int, input().split()))

dp = [[0] * (N + 1) for _ in range(N + 1)]
# 1 2 3 4
for leng in range(1, N + 1):
    for left in range(N - leng + 1):
        right = left + leng

        if (N - leng) % 2 == 0:
            dp[left][right] = max(
                dp[left + 1][right] + A[left], dp[left][right - 1] + A[right - 1]
            )
        else:
            dp[left][right] = min(
                dp[left + 1][right] - A[left], dp[left][right - 1] - A[right - 1]
            )

print(dp[0][N])
