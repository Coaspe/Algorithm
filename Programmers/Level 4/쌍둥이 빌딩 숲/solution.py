def solution(n, count):
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    dp[0][0] = 1

    MOD = 1_000_000_007

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i][j] = dp[i - 1][j - 1] + (2 * i - 2) * dp[i - 1][j]
            dp[i][j] %= MOD

    return dp[n][count]
