from sys import stdin
from collections import deque

input = stdin.readline
N, M = map(int, input().split())
recipes = [list(map(int, input().split())) for _ in range(M)]
L = int(input())
completed = set(map(int, input().split()))
G = [list() for _ in range(N + 1)]
degree = [0] * M

for i in range(M):
    recipe = recipes[i]
    k, r = recipe[0], recipe[-1]
    for j in range(1, k + 1):
        if recipe[j] not in completed:
            G[recipe[j]].append(i)
            degree[i] += 1

queue = deque([])

for i in range(M):
    if degree[i] == 0:
        queue.append(i)

while queue:
    i = queue.popleft()
    recipe = recipes[i]
    r = recipe[-1]
    if r in completed:
        continue
    completed.add(r)
    for j in G[r]:
        degree[j] -= 1
        if degree[j] == 0:
            queue.append(j)

print(len(completed))
print(*sorted(completed))
