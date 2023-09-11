import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, K = map(int, input().split())
LEVEL = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]  # 각각 연결되어있는 노드들을 저장

for i in range(N - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(node, level, parent):
    LEVEL[level] += 1
    for i in graph[node]:
        if i != parent:
            dfs(i, level + 1, node)


dfs(1, 0, -1)

ans = N

for i in range(N, -1, -1):
    if LEVEL[i] > K:
        ans -= LEVEL[i] - K
        LEVEL[i] = K

print(ans)
