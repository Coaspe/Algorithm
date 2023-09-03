N, K = map(int, input().split())
G = [input() for _ in range(N)]
A = [0] * N
# dp[i][j][k] = i 번째 아이템을 j 번 포지션을 바꾼 상태에서 현재 포지션이 k일 때 이길 수 있는 최대 값.
dp = [[[0] * 3 for _ in range(K + 2)] for _ in range(N + 1)]

for i in range(N):
    if G[i] == "H":
        A[i] = 0
    if G[i] == "P":
        A[i] = 1
    if G[i] == "S":
        A[i] = 2

for i in range(N):
    for j in range(K + 1):
        for k in range(3):
            if k == A[i]:
                dp[i][j][k] += 1

            dp[i + 1][j + 1][0] = max(dp[i + 1][j + 1][0], dp[i][j][k])
            dp[i + 1][j + 1][1] = max(dp[i + 1][j + 1][1], dp[i][j][k])
            dp[i + 1][j + 1][2] = max(dp[i + 1][j + 1][2], dp[i][j][k])

            dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k])

ans = 0

for i in range(3):
    ans = max(ans, dp[N - 1][K][i])

print(ans)
