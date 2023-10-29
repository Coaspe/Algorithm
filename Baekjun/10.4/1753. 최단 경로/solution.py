from heapq import heappush, heappop

# BOJ 1753. 최단 경로
V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

INF = float("inf")
dist = [INF] * (V + 1)
dist[K] = 0

q = [(0, K)]

while q:
    c, n = heappop(q)

    if dist[n] < c:
        continue

    for v, w in graph[n]:
        if dist[v] > c + w:
            dist[v] = c + w
            heappush(q, (dist[v], v))

for i in range(1, V + 1):
    print("INF" if dist[i] == INF else dist[i])
