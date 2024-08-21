from sys import stdin
from collections import defaultdict

input = stdin.readline


def getval(sx, sy, ex, ey):
    return (
        presum[ey][ex]
        - presum[sy - 1][ex]
        - presum[ey][sx - 1]
        + presum[sy - 1][sx - 1]
    )


n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
presum = [[0] * (n + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        presum[i][j] = (
            presum[i - 1][j]
            + presum[i][j - 1]
            - presum[i - 1][j - 1]
            + arr[i - 1][j - 1]
        )
ans = 0
for divy in range(1, n):
    for divx in range(1, n):
        dd = defaultdict(int)
        for i in range(1, divy + 1):
            for j in range(1, divx + 1):
                dd[getval(j, i, divx, divy)] += 1

        for i in range(divy + 1, n + 1):
            for j in range(divx + 1, n + 1):
                ans += dd[getval(divx + 1, divy + 1, j, i)]

        dd = defaultdict(int)

        for i in range(1, divy + 1):
            for j in range(divx + 1, n + 1):
                dd[getval(divx + 1, i, j, divy)] += 1

        for i in range(divy + 1, n + 1):
            for j in range(1, divx + 1):
                ans += dd[getval(j, divy + 1, divx, i)]

print(ans)
