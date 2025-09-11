from sys import stdin
from collections import deque

input = stdin.readline
M, N = map(int, input().split())

if N == 0:
    print(0)
    exit()

succ = [-1] * (N)
rev = [[] for _ in range(N)]

indegree = [0] * (N)

for _ in range(M):
    a, b = map(int, input().split())
    succ[a] = b
    rev[b].append(a)
    indegree[b] += 1

# Khan's algorithm
ans = [0] * (N)
Q = deque()

for i in range(N):
    if indegree[i] == 0:
        Q.append(i)
    if succ[i] == -1:
        ans[i] = 1


removed = [False] * (N)
while Q:
    x = Q.popleft()
    removed[x] = True
    y = succ[x]
    if y == -1:
        continue
    indegree[y] -= 1
    if indegree[y] == 0:
        Q.append(y)

# Find cycle
vis_circle = [False] * (N)

for i in range(N):
    if not removed[i] and not vis_circle[i]:
        # Start DFS
        stack = [i]
        while True:
            node = stack[-1]
            vis_circle[node] = True
            if vis_circle[succ[node]]:
                break
            stack.append(succ[node])

        for i in stack:
            ans[i] = len(stack)

q = deque([i for i in range(N) if ans[i] > 0])

while q:
    x = q.popleft()
    for y in rev[x]:
        if ans[y] == 0:
            ans[y] = ans[x] + 1
            q.append(y)

print(max(ans))
