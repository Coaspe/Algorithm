N, M, C = map(int, input().split())
dp = [
    [[[0] * (C + 1) for _ in range(C + 1)] for _ in range(M + 1)] for _ in range(N + 1)
]
MOD = 1_000_007

# dp[i][j][c][n] = (i, j)에 c가 최대 오락실 번호이면서 n번 방문했을 때 도착하는 경우의 수
B = [[0] * (M + 1) for _ in range(N + 1)]
dp[1][1][0][0] = 1
for i in range(C):
    r, c = map(int, input().split())
    if r == c == 1:
        dp[1][1][0][0] = 0
        dp[1][1][i + 1][1] = 1
    B[r][c] = i + 1

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if i == j == 1:
            continue

        if B[i][j]:
            for c in range(B[i][j]):
                for n in range(c + 1):
                    dp[i][j][B[i][j]][n + 1] += dp[i - 1][j][c][n]
                    dp[i][j][B[i][j]][n + 1] += dp[i][j - 1][c][n]
                    dp[i][j][B[i][j]][n + 1] %= MOD

        else:
            for c in range(C + 1):
                for n in range(c + 1):
                    dp[i][j][c][n] += dp[i - 1][j][c][n]
                    dp[i][j][c][n] += dp[i][j - 1][c][n]
                    dp[i][j][c][n] %= MOD

for i in range(C + 1):
    tmp = 0
    for j in range(C + 1):
        tmp += dp[-1][-1][j][i]
        tmp %= MOD
    print(tmp, end=" ")
