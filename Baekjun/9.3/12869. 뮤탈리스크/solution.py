from itertools import permutations
from collections import deque

N = int(input())

D = [9, 3, 1]
P = list(permutations(D))
A = list(map(int, input().split()))

while len(A) != 3:
    A.append(0)

MAX = 1e9 + 7
check = [[[MAX] * 61 for _ in range(61)] for _ in range(61)]

A.sort()

q = deque([(A, 0)])

while q:
    (a, b, c), cnt = q.popleft()

    if a == 0 and b == 0 and c == 0:
        print(cnt)
        break

    if cnt >= check[a][b][c]:
        continue

    check[a][b][c] = cnt

    for ac, bc, cc in P:
        newa = max(a - ac, 0)
        newb = max(b - bc, 0)
        newc = max(c - cc, 0)
        newa, newb, newc = sorted([newa, newb, newc])
        if check[newa][newb][newc] > cnt + 1:
            q.append(((newa, newb, newc), cnt + 1))
