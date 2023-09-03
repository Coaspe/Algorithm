import math

N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))


dp = [[0] * (K + 1) for _ in range(N + 1)]

largest = -1
space_used = 0

for i in range(1, N + 1):
    largest = max(largest, A[i])

    dp[i][0] = largest * i

    for j in range(1, K + 1):
        dp[i][j] = math.inf
        net_size = A[i]
        for c in range(i - 1, -1, -1):
            dp[i][j] = min(dp[i][j], dp[c][j - 1] + (i - c) * net_size)
            net_size = max(net_size, A[c])

    space_used += A[i]

print(dp[N][K] - space_used)
