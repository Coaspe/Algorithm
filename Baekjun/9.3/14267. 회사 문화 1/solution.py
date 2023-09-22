from sys import stdin
from collections import deque

input = stdin.readline

N, M = map(int, input().split())
up = list(map(int, input().split()))
down = [[] for _ in range(N + 1)]

for i in range(1, len(up)):
    down[up[i]].append(i + 1)

com = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    com[a] += b

q = deque([1])

while q:
    e = q.popleft()

    for n in down[e]:
        com[n] += com[e]
        q.append(n)

print(*com[1:])
