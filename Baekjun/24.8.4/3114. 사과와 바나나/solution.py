from sys import stdin

R, C = map(int, input().split())

input = stdin.readline
B = [list(input().split()) for _ in range(R)]

# A,B
pr = [[0] * C for _ in range(R)]
pc = [[0] * C for _ in range(R)]


for i in range(R):
    for j in range(C):
        if j > 0:
            pr[i][j] += pr[i][j - 1]
            if B[i][j - 1][0] == "A":
                pr[i][j] += int(B[i][j - 1][1:])
        if i > 0:
            pc[i][j] += pc[i - 1][j]
            if B[i - 1][j][0] == "B":
                pc[i][j] += int(B[i - 1][j][1:])
dp = [[0] * C for _ in range(R)]

for r in range(R):
    for c in range(C):
        if r > 0:
            dp[r][c] = dp[r - 1][c] + pr[r][c]
        if c > 0:
            dp[r][c] = max(dp[r][c], dp[r][c - 1] + pc[r][c])
        if r > 0 and c > 0:
            dp[r][c] = max(dp[r][c], dp[r - 1][c - 1] + pr[r][c] + pc[r][c])

print(dp[-1][-1])
