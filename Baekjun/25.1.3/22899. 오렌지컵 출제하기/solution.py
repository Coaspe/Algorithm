import sys
from heapq import *

myin = sys.stdin.readline

n, k = map(int, myin().split())

a = list(map(int, myin().split()))
b = list(map(int, myin().split()))

p = [[] for _ in range(n)]
q = [[] for _ in range(n)]

for i in range(n):
    p[a[i] - 1].append(b[i])

for i in p:
    i.sort()
    for j in range(len(i)):
        q[j].append(i[j])
pq = []
s = 0
for i in q:
    for j in i:
        if len(pq) < k:
            s += j
            heappush(pq, -j)
        elif -pq[0] > j:
            s += j + heappop(pq)
            heappush(pq, -j)
    print(s if len(pq) == k else -1, end=" ")
