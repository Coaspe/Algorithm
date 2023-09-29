import sys

input = sys.stdin.readline
n = int(input())
cost = []
MAX = 100000
dp = [MAX * 21 for _ in range(1 << n)]
for _ in range(n):
    cost.append(list(map(int, input().split())))
dp[0] = 0


for i in range(1 << n):
    cnt = 0
    j = i

    while j:
        j -= j & -j
        cnt += 1

    for j in range(n):
        if i & (1 << j):
            continue

        dp[i | (1 << j)] = min(dp[i | (1 << j)], dp[i] + cost[cnt][j])
print(dp[(1 << n) - 1])
