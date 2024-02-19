N, C = map(int, input().split())

# dp[i][j] -> i까지 봤을 때 j무게를 담는 경우의 수
dp = [[0] * (C + 1) for _ in range(N)]


A = list(map(int, input().split()))

dp[0][A[0]] = 1

for i in range(1, N):
    for j in range(C + 1):
        dp[i][j] = dp[i - 1][j]
        if j - A[i] >= 0:
            dp[i][j] += dp[i - 1][j - A[i]]

print(dp[-1][-1])
