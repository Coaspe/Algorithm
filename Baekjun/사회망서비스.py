import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline


def dfs(node):
    visited[node] = 1
    dp[node][0] = 1
    for child_node in tree[node]:
        if not visited[child_node]:
            dfs(child_node)
            dp[node][0] += min(dp[child_node][0], dp[child_node][1])
            dp[node][1] += dp[child_node][0]


N = int(input())
tree = [[] for _ in range(N + 1)]
dp = [[0, 0] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1)
answer = min(dp[1][0], dp[1][1])
print(answer)
