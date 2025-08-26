from sys import stdin
from heapq import heappop, heappush

input = stdin.readline

N, K = map(int, input().split())

J = [[] for _ in range(1000001)]

for _ in range(N):
    a, b = map(int, input().split())
    J[a].append(b)

bags = [int(input()) for _ in range(K)]

bags.sort()

hq = []

ans = now = 0

for bag in bags:
    while now <= bag:
        for j in J[now]:
            heappush(hq, -j)
        now += 1

    if hq:
        ans -= heappop(hq)

print(ans)
