N = int(input())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))

dp = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if A[i] > B[j]:
            dp[i][j] = dp[i - 1][j - 1] + 2
        elif A[i] < B[j]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j - 1] + 1
print(max(dp[-1]))
