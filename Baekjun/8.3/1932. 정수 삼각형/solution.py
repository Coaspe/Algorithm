N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]

dp[0][0] = arr[0][0]

for i in range(1, N):
    for j in range(i + 1):
        if i >= 1:
            dp[i][j] = max(dp[i][j], dp[i - 1][j])
        if i >= 1 and j >= 1:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1])

        dp[i][j] += arr[i][j]

print(max(dp[-1]))
