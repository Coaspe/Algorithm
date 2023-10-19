from sys import stdin
from heapq import heappush, heappop

input = stdin.readline
N = int(input())

L = [list(map(int, input().split())) for _ in range(N)]
L.sort(key=lambda x: (x[1], x[2]))

q = []

for i, j, k in L:
    if not q:
        heappush(q, (k, j, i))
        continue

    kk, jj, ii = heappop(q)

    if kk <= j:
        heappush(q, (k, j, i))
    else:
        heappush(q, (kk, jj, ii))
        heappush(q, (k, j, i))

print(len(q))
