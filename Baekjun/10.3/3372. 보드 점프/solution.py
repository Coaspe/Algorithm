from sys import stdin

input = stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
a, b = 0, 0

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            break
        if dp[i][j] > 0:
            a = board[i][j]
            if i + a < n:
                dp[i + a][j] += dp[i][j]
            if j + a < n:
                dp[i][j + a] += dp[i][j]
print(dp[-1][-1])
