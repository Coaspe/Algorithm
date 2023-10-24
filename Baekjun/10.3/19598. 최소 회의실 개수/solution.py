from heapq import heappush, heappop

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
L.sort()

q = []
for x, y in L:
    if q and q[0][0] <= x:
        heappop(q)
    heappush(q, [y, x])

print(len(q))
