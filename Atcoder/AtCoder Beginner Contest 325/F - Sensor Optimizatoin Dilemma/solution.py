# F - Sensor Optimization Dilemma
# https://atcoder.jp/contests/abc325/tasks/abc325_f


def solution():
    N = int(input())
    D = list(map(int, input().split()))

    L1, C1, K1 = map(int, input().split())
    L2, C2, K2 = map(int, input().split())

    # dp[i][j] = the minimum number of sensor 2 required to cover the first i segments,
    # when sensor 1 is used j times.
    dp = [[1e9] * (K1 + 1) for _ in range(N + 1)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(K1 + 1):
            rem = D[i]
            for k in range(j, K1 + 1):
                dp[i + 1][k] = min(dp[i + 1][k], dp[i][j] + (rem + L2 - 1) // L2)
                rem = max(rem - L1, 0)

    ans = 2e18

    for i in range(K1 + 1):
        if dp[N][i] > K2:
            continue
        ans = min(ans, i * C1 + dp[N][i] * C2)

    if ans > 1e18:
        ans = -1

    print(int(ans))


if __name__ == "__main__":
    solution()
