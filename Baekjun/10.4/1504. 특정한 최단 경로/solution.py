import heapq

N, E = map(int, input().split())

G = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))

v1, v2 = map(int, input().split())


def dijkstra(start):
    dist = [float("inf")] * (N + 1)
    dist[start] = 0
    q = [(0, start)]

    while q:
        d, now = heapq.heappop(q)

        if dist[now] < d:
            continue

        for next, cost in G[now]:
            if dist[next] > dist[now] + cost:
                dist[next] = dist[now] + cost
                heapq.heappush(q, (dist[next], next))

    return dist


dist_1 = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

ans = min(dist_1[v1] + dist_v1[v2] + dist_v2[N], dist_1[v2] + dist_v2[v1] + dist_v1[N])
if ans == float("inf"):
    print(-1)
else:
    print(ans)
