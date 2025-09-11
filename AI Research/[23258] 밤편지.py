from sys import stdin

input = stdin.readline
N, Q = map(int, input().split())
G = [None] + [[0, *list(map(int, input().split()))] for _ in range(N)]

query = [[] for _ in range(N + 2)]

for i in range(Q):
    c, s, e = map(int, input().split())
    query[c].append((s, e, i))
inf = float("inf")

dist = [[inf] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            dist[i][j] = 0
        elif G[i][j] > 0:
            dist[i][j] = G[i][j]

ans = [None] * Q
for c in range(1, N + 2):
    if c > 1:
        k = c - 1
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if i == j:
                    continue

                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    for s, e, idx in query[c]:
        ans[idx] = dist[s][e] if dist[s][e] != inf else -1

print("\n".join(map(str, ans)))
