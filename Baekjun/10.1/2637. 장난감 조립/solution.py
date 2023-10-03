from collections import defaultdict, deque

N = int(input())
M = int(input())

R = [list(map(int, input().split())) for _ in range(M)]

RR = [defaultdict(int) for _ in range(N + 1)]

G = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for x, y, k in R:
    indegree[x] += 1
    G[y].append((x, k))

q = deque()

for i in range(1, N + 1):
    if indegree[i] == 0:
        RR[i][i] = 1
        q.append(i)

while q:
    x = q.popleft()
    for n, k in G[x]:
        for key, val in RR[x].items():
            RR[n][key] += k * val
        indegree[n] -= 1

        if not indegree[n]:
            q.append(n)
ans = sorted(RR[-1].items(), key=lambda x: x[0])

for a, b in ans:
    print(a, b)
