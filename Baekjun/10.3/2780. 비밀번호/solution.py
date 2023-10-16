T = int(input())
G = [
    [7],
    [2, 4],
    [1, 3, 5],
    [2, 6],
    [1, 5, 7],
    [2, 4, 6, 8],
    [3, 5, 9],
    [0, 4, 8],
    [5, 7, 9],
    [6, 8],
]

MAX = 1234567

while T:
    T -= 1
    N = int(input())
    dp = [[0] * (N + 1) for _ in range(10)]

    for i in range(10):
        dp[i][1] = 1

    for j in range(2, N + 1):
        for i in range(10):
            for k in G[i]:
                dp[i][j] += dp[k][j - 1]
                dp[i][j] %= MAX
    ans = 0

    for i in range(10):
        ans += dp[i][N]

    print(ans % MAX)
