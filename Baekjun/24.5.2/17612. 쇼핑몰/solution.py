from heapq import heappop, heappush
from collections import deque
from sys import stdin

input = stdin.readline
N, K = map(int, input().split())

C = deque()
hq = []

for i in range(N):
    id, w = map(int, input().split())
    if K >= i + 1:
        heappush(hq, (w, (i + 1), id))
    else:
        C.append((w, id))

order = 1
ans = 0

while hq:
    t, n, id = heappop(hq)
    hq2 = [(-n, id)]

    while hq and hq[0][0] == t:
        t2, n2, id2 = heappop(hq)
        heappush(hq2, (-n2, id2))

    cahser = []
    while hq2:
        n, id = heappop(hq2)
        cahser.append(-n)
        ans += order * id
        order += 1

    while cahser and C:
        n = cahser.pop()
        w, iid = C.popleft()
        heappush(hq, (w + t, n, iid))

print(ans)

import heapq

n, k = map(int, input().split())
q = []
tmp = []
for m in range(n):
    i, w = map(int, input().split())
    if m < k:
        heapq.heappush(q, (w, m, i))
    else:
        w2, m, i2 = heapq.heappop(q)
        heapq.heappush(q, (w + w2, m, i))
        tmp.append((w2, m, i2))

tmp.extend(q)
tmp.sort(key=lambda x: (x[0], -x[1]))
print(sum((i + 1) * tmp[i][2] for i in range(len(tmp))))
