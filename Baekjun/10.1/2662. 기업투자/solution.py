M, N = map(int, input().split())
P = [[0] * N]

for _ in range(M):
    P.append(list(map(int, input().split()))[1:])

# dp[i][j] => 처음부터 i번째 기업까지 총 j원 투자했을 때
# 얻을 수 있는 최대 이익
dp = [[(0, [0]) for _ in range(M + 1)] for _ in range(N)]

for i in range(1, M + 1):
    dp[0][i] = (P[i][0], [i])

for i in range(1, N):
    for j in range(1, M + 1):
        for k in range(j + 1):
            dp[i][j] = max(
                dp[i][j],
                (dp[i - 1][j - k][0] + P[k][i], [*dp[i - 1][j - k][1], k]),
                key=lambda x: x[0],
            )

print(dp[-1][-1][0])
print(*dp[-1][-1][1])
