from heapq import *

N, M, K = map(int, input().split())

G = [[] for _ in range(N)]

for _ in range(M):
    u, v, c = map(int, input().split())
    u -= 1
    v -= 1

    G[v].append((u, c))

from sys import maxsize

inf = maxsize

dist = [inf] * N
q = []

for a in map(int, input().split()):
    a -= 1
    dist[a] = 0
    heappush(q, (0, a))

while q:
    cost, node = heappop(q)

    if cost > dist[node]:
        continue

    for next_node, next_cost in G[node]:
        new_cost = next_cost + cost

        if dist[next_node] > new_cost:
            dist[next_node] = new_cost
            heappush(q, (new_cost, next_node))

max_idx = 0

for i, v in enumerate(dist):
    if v > dist[max_idx]:
        max_idx = i

print(max_idx + 1)
print(dist[max_idx])
