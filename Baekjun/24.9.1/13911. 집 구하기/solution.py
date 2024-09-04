from heapq import *
from sys import maxsize, stdin

input = stdin.readline

V, E = map(int, input().split())
G = [{} for _ in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    if b in G[a]:
        G[a][b] = min(G[a][b], c)
    else:
        G[a][b] = c

    if a in G[b]:
        G[b][a] = min(G[b][a], c)
    else:
        G[b][a] = c


M, x = map(int, input().split())
MAC = set(map(int, input().split()))

S, y = map(int, input().split())
STA = set(map(int, input().split()))
inf = maxsize


def dij(start):
    dist = {}
    q = []

    for s in start:
        dist[s] = 0
        heappush(q, (0, s))

    while q:
        cost, node = heappop(q)

        if cost > dist[node]:
            continue

        for next_node, next_cost in G[node].items():
            new_cost = cost + next_cost

            if (not next_node in dist) or dist[next_node] > new_cost:
                dist[next_node] = new_cost
                heappush(q, (new_cost, next_node))

    return dist


MM = dij(MAC)
SS = dij(STA)

ans = inf
for i in range(1, V + 1):
    if i in MAC or i in STA:
        continue

    if (i in MM and MM[i] <= x) and (i in SS and SS[i] <= y):
        ans = min(ans, MM[i] + SS[i])

print(ans if ans != inf else -1)
