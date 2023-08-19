T = int(input())

while T:
    T -= 1
    input()
    B = [list(map(int, input().split())) for _ in range(2)]
    R, C = 2, len(B[0])
    dp = [[0] * C for _ in range(2)]

    dp[0][0] = B[0][0]
    dp[1][0] = B[1][0]

    if C > 1:
        dp[0][1] = dp[1][0] + B[0][1]
        dp[1][1] = dp[0][0] + B[1][1]

    for c in range(2, C):
        dp[0][c] = max(dp[1][c - 1], dp[1][c - 2]) + B[0][c]
        dp[1][c] = max(dp[0][c - 1], dp[0][c - 2]) + B[1][c]

    print(max(dp[0][-1], dp[1][-1]))
