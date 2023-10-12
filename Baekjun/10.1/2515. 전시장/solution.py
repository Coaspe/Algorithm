import sys

input = sys.stdin.readline
N, S = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(N)]
P.sort()
P.insert(0, [0, 0])

dp = [0] * (N + 1)
lim = [0] * (N + 1)


for i in range(1, N + 1):
    lim[i] = lim[i - 1]

    while lim[i] < i:
        if P[i][0] - P[lim[i]][0] < S:
            break
        lim[i] += 1

    lim[i] -= 1
    dp[i] = max(dp[i - 1], dp[lim[i]] + P[i][1])

print(dp[-1])
