import sys

input = lambda: map(int, sys.stdin.readline().split())
N, Q = input()
graph = [[] for _ in range(N + 1)]
degree = [0 for _ in range(N + 1)]

for _ in range(N):
    a, b = input()
    degree[a] += 1
    degree[b] += 1
    graph[a].append(b)
    graph[b].append(a)

visited = [-1 for _ in range(N + 1)]
q = [i for i, v in enumerate(degree) if v == 1]

while q:
    nq = []
    for cur in q:
        for nxt in graph[cur]:
            if visited[nxt] == -1:
                visited[cur] = nxt
                degree[nxt] -= 1
                if degree[nxt] == 1:
                    nq.append(nxt)
    q = nq


def zp(x):
    if visited[x] == x:
        return x

    if visited[x] == -1:
        visited[x] = x
        return x

    visited[x] = zp(visited[x])
    return visited[x]


for i in range(1, N + 1):
    zp(i)

ans = []
for _ in range(Q):
    u, v = input()

print("\n".join(ans))
