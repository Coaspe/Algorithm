import sys

inf = 10**9

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    dp = [10**9] * (N + 1)

    info = [list(map(int, input().split())) for _ in range(M)]
    info.sort(key=lambda x: x[1])

    dp[0] = 0
    for s, p, o in info:
        for j in range(N - 1, -1, -1):
            temp = min(N, j + s)
            dp[temp] = min(dp[temp], dp[j] + o + (temp - j) * p)

    print(dp[N])
