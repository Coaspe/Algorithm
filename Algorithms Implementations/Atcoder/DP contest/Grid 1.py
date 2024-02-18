import sys

input = sys.stdin.readline
MOD = 10**9 + 7
R, C = map(int, input().split())
B = [input() for _ in range(R)]

dp = [[0] * C for _ in range(R)]
dp[0][0] = 1

for r in range(R):
    for c in range(C):
        if r < R - 1 and B[r + 1][c] == ".":
            dp[r + 1][c] = (dp[r + 1][c] + dp[r][c]) % MOD
        if c < C - 1 and B[r][c + 1] == ".":
            dp[r][c + 1] = (dp[r][c + 1] + dp[r][c]) % MOD

print(dp[R - 1][C - 1])
