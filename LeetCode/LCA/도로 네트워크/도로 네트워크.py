import sys
import collections
import math

input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))
LOG = 21

n = int(input())
dp = [[[0, 0, 0] for _ in range(LOG)] for _ in range(n+1)]
d = [0] * (n+1)
graph = collections.defaultdict(list)

for _ in range(n-1):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))


def dfs(node, depth):
    d[node] = depth
    for child, cost in graph[node]:
        if not d[child]:
            dp[child][0] = [node, cost, cost]
            dfs(child, depth + 1)


def set_dp():
    dfs(1, 0)
    for i in range(1, LOG):
        for j in range(1, n+1):
            dp[j][i][0] = dp[dp[j][i-1][0]][i-1][0]
            dp[j][i][1] = min(
                dp[j][i-1][1], dp[dp[j][i-1][0]][i-1][1])
            dp[j][i][2] = max(
                dp[j][i-1][2], dp[dp[j][i-1][0]][i-1][2])

# b 노드에서 2^i 번째 부모까지 가장 큰, 작은 비용


def lca(a, b):
    lo, hi = math.inf, -math.inf

    if d[a] > d[b]:
        a, b = b, a
    # 높이 맞추기
    for i in range(LOG-1, -1, -1):
        if d[b] - d[a] >= (1 << i):
            lo = min(dp[b][i][1], lo)
            hi = max(dp[b][i][2], hi)
            b = dp[b][i][0]

    if a == b:
        return lo, hi

    for i in range(LOG-1, -1, -1):
        if dp[a][i][0] != dp[b][i][0]:
            lo = min(dp[a][i][1], dp[b][i][1], lo)
            hi = max(dp[a][i][2], dp[b][i][2], hi)
            a = dp[a][i][0]
            b = dp[b][i][0]

    return (min(lo, dp[a][0][1], dp[b][0][1]), max(hi, dp[a][0][2], dp[b][0][2]))


set_dp()

Q = int(input())

for _ in range(Q):
    ancestor = lca(*map(int, input().split()))
    print(f"{ancestor[0]} {ancestor[1]}")
