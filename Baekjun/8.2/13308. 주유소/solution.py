import sys, heapq


def dijkstra():
    # node에 도착할 때까지 체크한 경로의 최소 비용이 cost인 경로의 거리의 합
    dist = [[sys.maxsize] * (max(city) + 1) for _ in range(n + 1)]
    min_cost = [sys.maxsize] * (n + 1)

    heap, dist[1][city[1]] = [], 0
    heapq.heappush(heap, (0, 1, city[1]))
    min_cost[1] = city[1]

    while heap:
        distance, node, cost = heapq.heappop(heap)

        if node == n:
            return distance

        if distance > dist[node][cost] or cost > min_cost[node]:
            continue

        min_cost[node] = cost

        for next_node, next_weight in adj[node]:
            new_dist = distance + cost * next_weight
            if dist[next_node][cost] > new_dist:
                dist[next_node][cost] = new_dist
                heapq.heappush(
                    heap,
                    (
                        new_dist,
                        next_node,
                        min(cost, city[next_node]),
                    ),
                )


n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
city = [0] + list(map(int, sys.stdin.readline().split()))
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

print(dijkstra())

"""
"""
# import sys

# input = sys.stdin.readline
# MIS = lambda: map(int, input().split())
# import heapq

# INF = 10**13

# """
# 노드 x에서 모든 노드로 가는 최단 거리를 구한다.
# """


# def dijkstra(x):
#     if fee[x] >= fee[0]:
#         if x:
#             return
#     dis = [INF] * N
#     dis[x] = 0
#     heap = [(0, x)]
#     while heap:
#         cd, cn = heapq.heappop(heap)
#         for nn, nd in graph[cn]:
#             cost = cd + nd
#             if cost < dis[nn]:
#                 dis[nn] = cost
#                 if fee[nn] >= fee[x]:
#                     heapq.heappush(heap, (cost, nn))
#     nf = fee[x]
#     for i in range(N):
#         if fee[i] < nf:
#             Lgraph[x].append((i, dis[i]))
#     return


# """
# dijkstra로 한 노드에서 다른 노드들로 가는 최단 거리를 구하고,
# 갈 수 있으면 바로 점프
# """


# def dijkstra2():
#     dis = [INF] * N
#     dis[0] = 0
#     heap = [(0, 0)]
#     while heap:
#         cd, cn = heapq.heappop(heap)

#         if cd > dis[-1]:
#             break

#         if not work[cn]:
#             work[cn] = 1
#             dijkstra(cn)

#         for nn, nd in Lgraph[cn]:
#             nf = nd * fee[cn]
#             cost = cd + nf
#             if cost < dis[nn]:
#                 dis[nn] = cost
#                 heapq.heappush(heap, (cost, nn))
#     return dis[-1]


# N, M = MIS()
# fee = list(MIS())
# fee[-1] = 0
# graph = [[] for _ in range(N)]
# for _ in range(M):
#     a, b, w = MIS()
#     a -= 1
#     b -= 1
#     if a != N - 1:
#         graph[a].append((b, w))
#     if b != N - 1:
#         graph[b].append((a, w))

# Lgraph = [[] for _ in range(N)]
# work = [0] * N
# work[-1] = 1
# print(dijkstra2())
