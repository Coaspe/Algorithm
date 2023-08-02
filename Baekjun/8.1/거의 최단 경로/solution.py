import sys
import heapq
from collections import deque

INF = sys.maxsize

while True:
    n, m = map(int, sys.stdin.readline().rstrip().split())
    if n == 0 and m == 0:
        break
    nodes = [[] for _ in range(n)]
    nodes_inv = [[] for _ in range(n)]
    edges = [[False for _ in range(n)] for _ in range(n)]
    s, d = map(int, sys.stdin.readline().rstrip().split())

    for _ in range(m):
        u, v, p = map(int, sys.stdin.readline().rstrip().split())
        nodes[u].append([v, p])
        nodes_inv[v].append([u, p])

    def Dijstra():
        distances = [INF for _ in range(n)]
        distances[s] = 0

        pq = []
        heapq.heappush(pq, [0, s])

        while pq:
            cur_cost, cur_node = heapq.heappop(pq)

            if distances[cur_node] < cur_cost:
                continue

            for next_node, next_cost in nodes[cur_node]:
                if edges[cur_node][next_node]:
                    continue
                if distances[next_node] > next_cost+cur_cost:
                    distances[next_node] = next_cost+cur_cost
                    heapq.heappush(pq, [next_cost+cur_cost, next_node])

        return distances

    def BFS():
        queue = deque()
        queue.append(d)

        while queue:
            cur_node = queue.popleft()

            if cur_node == s:
                continue

            for post_node, post_cost in nodes_inv[cur_node]:
                if distances[post_node] + post_cost == distances[cur_node] and not edges[post_node][cur_node]:
                    # cur_node로 향하는 이전 간선 비용을 사용했을 때 distances에 기록된 비용이라면 곧 최단 경로에 사용했다는 뜻이다.
                    edges[post_node][cur_node] = True
                    queue.append(post_node)

    distances = Dijstra()
    BFS()
    distances = Dijstra()
    if distances[d] == INF:
        print(-1)
    else:
        print(distances[d])
