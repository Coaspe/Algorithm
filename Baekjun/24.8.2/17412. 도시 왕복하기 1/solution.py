import sys
from collections import deque

input = sys.stdin.readline
MAX = 1e9


def fordFulkerson(graph, s, t, n):
    remain = [[0] * n for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            remain[i][j] = graph[i][j]

    while True:
        visited = [False] * n
        queue = deque()
        queue.append(s)
        visited[s] = True
        path = [-1] * n

        while queue:
            a = queue.popleft()
            for b in range(n):
                if not visited[b] and remain[a][b] > 0:
                    queue.append(b)
                    path[b] = a
                    visited[b] = True
                    if b == t:
                        break
            if visited[t]:
                break

        if not visited[t]:
            break

        ans += 1
        b = t
        min_remain = MAX

        while b != s:
            a = path[b]
            min_remain = min(min_remain, remain[a][b])
            b = a

        b = t
        while b != s:
            a = path[b]
            remain[a][b] -= min_remain
            remain[b][a] += min_remain
            b = a
    return ans


N, P = map(int, input().split())
G = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(P):
    a, b = map(int, input().split())
    G[a][b] = 1

print(fordFulkerson(G, 1, 2, N + 1))
