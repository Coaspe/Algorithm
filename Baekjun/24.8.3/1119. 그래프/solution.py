from collections import deque

N = int(input())
G = [[] for _ in range(N)]

for i in range(N):
    for j, v in enumerate(list(input())):
        if v == "Y":
            G[i].append(j)

if N == 1:
    print(0)
    exit(0)
g_edges = 0


def dfs(node):
    nodes = 0
    edges = 0
    q = deque([node])

    while q:
        n = q.popleft()
        nodes += 1
        for next_node in G[n]:
            edges += 1
            if C[next_node]:
                continue
            C[next_node] = 1
            q.append(next_node)

    if nodes == 1:
        print(-1)
        exit(0)

    return edges // 2 - (nodes - 1)


C = [0] * N
groups = 0
for i in range(N):
    if C[i]:
        continue

    C[i] = 1
    groups += 1
    g_edges += dfs(i)

print(groups - 1 if g_edges >= groups - 1 else -1)
