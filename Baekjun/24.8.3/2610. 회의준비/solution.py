N = int(input())
M = int(input())


G = [[] for _ in range(N)]

from sys import maxsize

inf = maxsize
dist = [[inf] * N for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
    dist[a][b] = 1
    dist[b][a] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue

            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

C = [0] * N
ans_g = 0
ans_p = []

for i in range(N):
    if C[i]:
        continue

    ans_g += 1
    C[i] = 1

    candid = [i]

    for j in range(i + 1, N):
        if dist[i][j] != inf and not C[j]:
            candid.append(j)
            C[j] = 1

    ans_idx, ans_v = -1, inf

    for j in candid:
        tmp_v = 0
        for k in candid:
            if dist[j][k] != inf and dist[j][k] > tmp_v:
                tmp_v = dist[j][k]

        if ans_v > tmp_v:
            ans_idx = j
            ans_v = tmp_v

    ans_p.append(ans_idx + 1)

print(ans_g)

for p in sorted(ans_p):
    print(p)
