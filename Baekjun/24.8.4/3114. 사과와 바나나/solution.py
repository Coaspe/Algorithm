import sys
from collections import deque

input = sys.stdin.readline


n, l = map(int, input().split())
vis = [0] * (n + 1)
rvis = [0] * (l + 1)
rail = [list(map(int, input().split())) for _ in range(l)]
g = [[] for _ in range(n + 1)]

for i in range(l):
    for j in rail[i]:
        if j == -1:
            break
        g[j].append(i)


st, en = map(int, input().split())


q = deque()

q.append(st)
vis[st] = 1
flag = 0
while q:
    cur = q.popleft()

    if cur == en:

        if st == en:
            print(0)

        else:
            print(vis[cur] - 2)
        flag = 1
        break

    for i in g[cur]:
        if vis[i]:
            continue
        for j in rail[i]:
            if vis[j] or j == -1:
                continue
            vis[j] = vis[cur] + 1
            q.append(j)


if not flag:
    print(-1)
