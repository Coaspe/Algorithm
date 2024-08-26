from math import sqrt


def heron(a, b, c):
    t = max(a, b, c)
    val = sum([a, b, c])
    if 2 * t >= val:
        return -1
    s = val / 2
    return sqrt(s * (s - a) * (s - b) * (s - c))


N = int(input())
A = list(map(int, input().split()))
dp = [-1] * (1 << N)


def solve(state):
    if dp[state] != -1:
        return dp[state]

    dp[state] = 0

    for i in range(N - 2):
        if state & (1 << i):
            continue
        for j in range(i + 1, N - 1):
            if state & (1 << j):
                continue
            for k in range(j + 1, N):
                if state & (1 << k):
                    continue
                area = heron(A[i], A[j], A[k])
                if area == -1:
                    continue

                dp[state] = max(
                    dp[state], area + solve(state | (1 << i) | (1 << j) | (1 << k))
                )

    return dp[state]


print(solve(0))
