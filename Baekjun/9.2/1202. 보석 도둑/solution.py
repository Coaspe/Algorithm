import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N, K = map(int, input().split())
J = [tuple(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

q = []
ans = 0

J.sort(reverse=True)
bags.sort()

for b in bags:
    while J and J[-1][0] <= b:
        j = J.pop()
        heappush(q, (-j[1], j[0]))
    if q:
        ans -= heappop(q)[0]

print(ans)

#####################################################
import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())

jewelry = [[] for _ in range(int(1e6) + 1)]

for _ in range(n):
    a, b = map(int, input().split())
    jewelry[a].append(b)

bags = []
for _ in range(k):
    heapq.heappush(bags, int(input()))

jewerly_box = []
answer = 0
now = 0
for _ in range(k):
    bag = heapq.heappop(bags)

    while now <= bag:
        for jewelr in jewelry[now]:
            heapq.heappush(jewerly_box, -jewelr)
        now += 1

    if jewerly_box:
        answer -= heapq.heappop(jewerly_box)

print(answer)
