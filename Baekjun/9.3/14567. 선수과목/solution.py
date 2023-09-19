from collections import deque
from sys import stdin

input = stdin.readline

N, M = map(int, input().split())

outdegree = [0] * N
q = deque()
G = [[] for _ in range(N)]
time = 1
ans = [-1] * N

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    outdegree[b] += 1
    G[a].append(b)

for i in range(N):
    if outdegree[i] == 0:
        q.append(i)

while N:
    tmp_q = deque()
    while q:
        x = q.popleft()
        N -= 1
        ans[x] = time
        for node in G[x]:
            outdegree[node] -= 1

            if outdegree[node] == 0:
                tmp_q.append(node)
    q = tmp_q
    time += 1
print(*ans)
