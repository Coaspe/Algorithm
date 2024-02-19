N = int(input())
ary = list(map(int, input().split()))
ary.insert(0, 0)
GAPS = 250_000

# dp[i][j] => i번째까지 블록을 사용할 수 있을 때, 두 탑의 차이가 j이면서 작은 탑의 높이가 최대인 값을 저장한다.
dp = [[0] * (GAPS + 1) for _ in range(N + 1)]

for i in range(1, GAPS):
    dp[0][i] = -1

for i in range(1, N + 1):
    for j in range(GAPS + 1):
        dp[i][j] = dp[i - 1][j]

        if j - ary[i] >= 0 and dp[i - 1][j - ary[i]] != -1:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - ary[i]] + ary[i])
        if ary[i] - j >= 0 and dp[i - 1][ary[i] - j] != -1:
            dp[i][j] = max(dp[i][j], dp[i - 1][ary[i] - j] + j)
        if j + ary[i] <= GAPS and dp[i - 1][j + ary[i]] != -1:
            dp[i][j] = max(dp[i][j], dp[i - 1][j + ary[i]])

print(dp[N][0] if dp[N][0] else -1)
