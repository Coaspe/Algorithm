from heapq import *

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))

S, E = map(int, input().split())
p = int(input())
P = list(map(int, input().split())) + [S, E]

inf = float("inf")

dist = [[0] * (p + 2) for _ in range(p + 2)]


def dji(start):
    dist = [inf] * (N + 1)
    dist[0] = 0
    hq = [(0, start)]

    while hq:
        cost, node = heappop(hq)

        if cost > dist[node]:
            continue

        for nnode, ncost in G[node]:
            nncost = ncost + cost

            if nncost >= dist[nnode]:
                continue

            heappush(hq, (nncost, nnode))
            dist[nnode] = nncost

    return dist


for i in range(p + 2):
    dd = dji(P[i])

    for j in range(p + 2):
        dist[i][j] = dd[P[j]]

dp = [[-1] * (1 << p) for _ in range(p + 1)]


def dfs(now, state):
    if state + 1 == 1 << p:
        if dist[now][-1]:
            return dist[now][-1]
        return inf

    if dp[now][state] != -1:
        return dp[now][state]

    min_val = inf
    for pp in range(p):
        if not dist[now][pp] or state & (1 << pp):
            continue

        min_val = min(min_val, dfs(pp, state | 1 << pp) + dist[now][pp])

    dp[now][state] = min_val
    return min_val


ans = dfs(p, 0)
print(ans if ans != inf else -1)
