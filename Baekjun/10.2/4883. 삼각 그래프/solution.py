MAX = 1_000_000
T = 0
while True:
    T += 1
    N = int(input())
    if not N:
        break

    B = [list(map(int, input().split())) for _ in range(N)]
    dp = [[MAX] * 3 for _ in range(N)]

    dp[0][1] = B[0][1]
    dp[0][2] = B[0][1] + B[0][2]

    for i in range(1, N):
        dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + B[i][0]
        dp[i][1] = min(dp[i][0], dp[i - 1][1], dp[i - 1][0], dp[i - 1][2]) + B[i][1]
        dp[i][2] = min(dp[i][1], dp[i - 1][1], dp[i - 1][2]) + B[i][2]

    print(f"{T}. {dp[-1][1]}")
