from collections import defaultdict
import heapq
import math
V, E = map(int, input().split())
dist = [[math.inf]*(V+1) for _ in range(V+1)]
graph = defaultdict(list)
q = []
for _ in range(E):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    dist[a][b] = d
    heapq.heappush(q, (d, a, b))


while q:
    c, s, d = heapq.heappop(q)

    if s == d:
        print(c)
        break
    if c > dist[s][d]:
        continue

    for nex, cost in graph[d]:
        newCost = c + cost
        if dist[s][nex] > newCost:
            dist[s][nex] = newCost
            heapq.heappush(q, (newCost, s, nex))
else:
    print(-1)
