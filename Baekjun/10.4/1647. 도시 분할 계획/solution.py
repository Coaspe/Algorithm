import heapq
from sys import stdin

input = stdin.readline

N, M = map(int, input().split())

G = [[] for _ in range(N)]

for _ in range(M):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append((b, w))
    G[b].append((a, w))


def prim(G):
    n = len(G)
    heap = [(0, 0)]
    in_mst = [False] * n
    mst_cost = 0
    max_cost = 0
    edges_used = 0

    while edges_used < n:
        weight, curr_node = heapq.heappop(heap)

        if in_mst[curr_node]:
            continue

        in_mst[curr_node] = True
        mst_cost += weight
        max_cost = max(max_cost, weight)
        edges_used += 1

        for next_node, next_weight in G[curr_node]:
            if not in_mst[next_node]:
                heapq.heappush(heap, (next_weight, next_node))

    return mst_cost - max_cost


print(prim(G))
