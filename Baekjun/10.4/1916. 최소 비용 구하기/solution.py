from heapq import heappush, heappop

# BOJ 1916. 최소비용 구하기
N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
start, end = map(int, input().split())

INF = float("inf")
dist = [INF] * (N + 1)
dist[start] = 0

q = [(0, start)]

while q:
    c, n = heappop(q)

    if dist[n] < c:
        continue

    for v, w in graph[n]:
        if dist[v] > c + w:
            dist[v] = c + w
            heappush(q, (dist[v], v))

print(dist[end])
