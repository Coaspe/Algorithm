import math
import heapq

# 총 N개 도로 M개 추종자 K명
N, M, K = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

P = list(map(int, input().split()))


def dij(starts):
    q = []
    dist = [math.inf] * (N + 1)

    for s in starts:
        dist[s] = 0
        q.append((0, s))

    while q:
        c, n = heapq.heappop(q)

        if c > dist[n]:
            continue

        for next_node, next_cost in graph[n]:
            new_cost = next_cost + c
            if dist[next_node] > new_cost:
                dist[next_node] = new_cost
                heapq.heappush(q, (new_cost, next_node))

    return dist


baek = dij([1])
P = dij(P)
ans = [i for i in range(2, N + 1) if P[i] > baek[i]]

if ans:
    print(*ans)
else:
    print(0)
