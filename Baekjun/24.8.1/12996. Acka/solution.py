S, A, B, C = map(int, input().split())

dp = [
    [[[-1] * (C + 1) for _ in range(B + 1)] for _ in range(A + 1)] for _ in range(S + 1)
]

MOD = 1_000_000_007


def go(s, a, b, c):
    if s == 0:
        if a == b == c == 0:
            return 1
        else:
            return 0
    if a < 0 or b < 0 or c < 0:
        return 0

    if dp[s][a][b][c] != -1:
        return dp[s][a][b][c]

    dp[s][a][b][c] = 0
    dp[s][a][b][c] += go(s - 1, a - 1, b, c)
    dp[s][a][b][c] += go(s - 1, a, b - 1, c)
    dp[s][a][b][c] += go(s - 1, a, b, c - 1)
    dp[s][a][b][c] += go(s - 1, a - 1, b - 1, c)
    dp[s][a][b][c] += go(s - 1, a, b - 1, c - 1)
    dp[s][a][b][c] += go(s - 1, a - 1, b, c - 1)
    dp[s][a][b][c] += go(s - 1, a - 1, b - 1, c - 1)
    dp[s][a][b][c] %= MOD
    return dp[s][a][b][c]


print(go(S, A, B, C))
