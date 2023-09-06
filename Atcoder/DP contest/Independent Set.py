import sys

sys.setrecursionlimit(1000000)
"""
Simple tree DP
"""
N = int(input())
adj = [[] for _ in range(N)]
MOD = 10**9 + 7

for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].append(b)
    adj[b].append(a)

dp = [[-1, -1] for _ in range(N)]


def dfs(node, BW, prev):
    if dp[node][BW] != -1:
        return dp[node][BW]

    ret = 1
    for next_node in adj[node]:
        if prev == next_node:
            continue
        ret *= ((dfs(next_node, 1, node) + BW * dfs(next_node, 0, node)) % MOD) % MOD
    dp[node][BW] = ret
    return dp[node][BW]


print((dfs(0, 0, -1) + dfs(0, 1, -1)) % MOD)
