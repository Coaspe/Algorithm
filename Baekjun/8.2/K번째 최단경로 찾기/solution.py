from sys import maxsize as MAX
import heapq

n, m, k = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


hq = [(0, 1)]

dist = [[MAX] * k for _ in range(n + 1)]

dist[1][0] = 0

while hq:
    cost, node = heapq.heappop(hq)

    if cost > dist[node][k - 1]:
        continue

    for next_node, new_cost in graph[node]:
        next_cost = new_cost + cost

        if dist[next_node][k - 1] <= next_cost:
            continue

        dist[next_node][k - 1] = next_cost
        dist[next_node].sort()
        heapq.heappush(hq, (next_cost, next_node))

for i in range(1, n + 1):
    if dist[i][k - 1] != MAX:
        print(dist[i][k - 1])
    else:
        print(-1)
