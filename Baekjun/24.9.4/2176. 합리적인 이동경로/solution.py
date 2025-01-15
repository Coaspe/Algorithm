from heapq import heappop, heappush

N, M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append((b, w))
    G[b].append((a, w))

inf = float("inf")

DE = [inf] * N


def dij(start, dist):
    dist[start] = 0

    q = [(0, start)]

    while q:
        d, n = heappop(q)

        if d > dist[n]:
            continue

        for next_node, cost in G[n]:
            new_dist = d + cost
            if dist[next_node] > new_dist:
                dist[next_node] = new_dist
                heappush(q, (new_dist, next_node))


dij(1, DE)

dp = [-1] * N


def dfs(node):
    if node == 1:
        return 1

    if dp[node] > -1:
        return dp[node]

    cc = 0
    for next_node, _ in G[node]:
        if DE[node] > DE[next_node]:
            cc += dfs(next_node)

    dp[node] = cc

    return cc


print(dfs(0))
