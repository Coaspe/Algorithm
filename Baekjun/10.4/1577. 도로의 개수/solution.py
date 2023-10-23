N, M = map(int, input().split())
K = int(input())
checked = set()

for _ in range(K):
    a, b, c, d = map(int, input().split())
    x = sorted([(a, b), (c, d)])
    checked.add((*x[0], *x[1]))

dp = [[0] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i in range(N + 1):
    for j in range(M + 1):
        if i == j == 0:
            continue
        if (i - 1, j, i, j) not in checked:
            dp[i][j] += dp[i - 1][j]
        if (i, j - 1, i, j) not in checked:
            dp[i][j] += dp[i][j - 1]
print(dp[-1][-1])
