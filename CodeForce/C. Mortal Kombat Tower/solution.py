import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    # If we define dp[i][j] as the minimum number of skip points needed to get to the
    # jth boss on player i's turn (our turn is zero), then our transitions would be:
    # i번째 플레이어가 j번째 보스와 상대할 수 있을 때까지 필요한 skip points.
    n = len(a)
    dp = [[math.inf] * (n + 1) for _ in range(2)]

    dp[1][0] = 0

    for i in range(n):
        dp[0][i + 1] = min(dp[0][i + 1], dp[1][i] + a[i])
        dp[1][i + 1] = min(dp[1][i + 1], dp[0][i])

        if i + 2 <= n:
            dp[0][i + 2] = min(dp[0][i + 2], dp[1][i] + a[i] + a[i + 1])
            dp[1][i + 2] = min(dp[1][i + 2], dp[0][i])

    print(min(dp[0][n], dp[1][n]))
