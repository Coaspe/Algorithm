N, T = map(int, input().split())
KS = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]

# dp[i][j] => i 단원까지 봤을 떄, j 시간을 사용했을 때 얻을 수 있는 최대 점수.
dp = [[0 for _ in range(T + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, T + 1):
        dp[i][j] = dp[i - 1][j]
        if j - KS[i][0] >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - KS[i][0]] + KS[i][1])

print(dp[-1][-1])
