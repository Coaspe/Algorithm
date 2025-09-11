from sys import stdin

input = stdin.readline
inf = float("inf")
K, N, M = map(int, input().split())

G = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, t, h = map(int, input().split())
    G[a].append((b, t, h))
    G[b].append((a, t, h))

start, end = map(int, input().split())


from heapq import *


def dij():
    dist = [[inf] * (K + 1) for _ in range(N + 1)]
    dist[start][K] = 0

    hq = [(0, start, K)]

    while hq:
        cost, node, k = heappop(hq)

        if cost > dist[node][k]:
            continue

        for next_node, next_time, next_wood in G[node]:
            new_cost = cost + next_time

            if k - next_wood > 0 and dist[next_node][k - next_wood] > new_cost:
                dist[next_node][k - next_wood] = new_cost
                heappush(hq, (new_cost, next_node, k - next_wood))

    return min(dist[end])


ans = dij()

if ans == inf:
    print(-1)
else:
    print(ans)
