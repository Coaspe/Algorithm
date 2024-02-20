from collections import deque
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
indegree = [0] * (N + 1)
parent = [set() for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]

for _ in range(K):
    a, b = map(int, input().split())
    indegree[b] += 1
    graph[a].append(b)

que = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        que.append(i)

while que:
    node = que.popleft()
    for nxt in graph[node]:
        indegree[nxt] -= 1
        parent[nxt] |= parent[node] | {node}
        if indegree[nxt] == 0:
            que.append(nxt)

S = int(input())
for _ in range(S):
    a, b = map(int, input().split())
    if a in parent[b]:
        print(-1)
    elif b in parent[a]:
        print(1)
    else:
        print(0)
