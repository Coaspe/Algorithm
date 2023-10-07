N, M = map(int, input().split())

MIN = -3276800

# dp = [[0] + [MIN] * (M) for _ in range(N + 1)]

# total = 0
# prefix = [0]

# for _ in range(N):
#     total += int(input())
#     prefix.append(total)

# for i in range(1, N + 1):
#     for j in range(1, M + 1):
#         dp[i][j] = dp[i - 1][j]
#         for k in range(1, i + 1):
#             if k >= 2:
#                 dp[i][j] = max(dp[i][j], dp[k - 2][j - 1] + prefix[i] - prefix[k - 1])
#             elif k == 1 and j == 1:
#                 dp[i][j] = max(dp[i][j], prefix[i])
# print(dp[N][M])

con = [[0] + [MIN] * M for _ in range(N + 1)]
noncon = [[0] + [MIN] * M for _ in range(N + 1)]

for i in range(1, N + 1):
    n = int(input())
    for j in range(1, min(M, (i + 1) // 2) + 1):
        noncon[i][j] = max(noncon[i - 1][j], con[i - 1][j])
        con[i][j] = max(con[i - 1][j], noncon[i - 1][j - 1]) + n

print(max(con[-1][-1], noncon[-1][-1]))
