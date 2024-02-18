import sys

sys.setrecursionlimit(1000000)
N, M = map(int, input().split())
adj = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].append(b)

dp = [-1] * N


def dfs(n):
    if dp[n] != -1:
        return dp[n]

    mx = 0
    for next_node in adj[n]:
        mx = max(mx, dfs(next_node))

    dp[n] = mx + int(len(adj[n]) != 0)

    return dp[n]


for i in range(N):
    dfs(i)

print(max(dp))
