from heapq import *
from sys import maxsize

inf = maxsize
N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))

hq = []
dist = [[inf, ""] for _ in range(N + 1)]
dist[1] = [0, "1"]
hq = [(0, 1, "1")]

while hq:
    cost, node, path = heappop(hq)

    if cost > dist[node][0]:
        continue

    for next_node, next_cost in G[node]:
        new_cost = next_cost + cost

        if dist[next_node][0] > new_cost:
            dist[next_node] = [new_cost, path + "/" + str(next_node)]
            heappush(hq, (new_cost, next_node, dist[next_node][-1]))

if dist[-1][0] == inf:
    print(-1)
    exit(0)


def dij(a, b):
    hq = []
    dist = [inf] * (N + 1)
    dist[1] = 0
    hq = [(0, 1)]

    while hq:
        cost, node = heappop(hq)

        if cost > dist[node]:
            continue

        for next_node, next_cost in G[node]:
            if (a == next_node and b == node) or (b == next_node and a == node):
                continue

            new_cost = next_cost + cost

            if dist[next_node] > new_cost:
                dist[next_node] = new_cost
                heappush(hq, (new_cost, next_node))

    return dist[-1]


ans = 0
D = list(dist[-1][1].split("/"))
for i in range(len(D) - 1):
    tmp = dij(int(D[i]), int(D[i + 1]))

    if tmp == inf:
        print(-1)
        exit(0)

    ans = max(ans, tmp)

print(ans - dist[-1][0])
