import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline


def dfs(node):
    visited[node] = 1
    dp[node][0] = cost[node-1]
    for child_node in tree[node]:
        if not visited[child_node]:
            dfs(child_node)
            dp[node][0] += dp[child_node][1]
            dp[node][1] += max(dp[child_node])


N = int(input())
cost = list(map(int, input().split()))
tree = [[] for _ in range(N + 1)]
dp = [[0, 0] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1)
answer = max(dp[1])
print(answer)
