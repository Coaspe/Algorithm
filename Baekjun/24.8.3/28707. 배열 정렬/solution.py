from heapq import *

N = int(input())
A = []

for a in map(int, input().split()):
    A.append(str(a - 1))

M = int(input())
C = {}


def check_order(s):
    for i in range(N - 1):
        if int(s[i]) > int(s[i + 1]):
            return False
    return True


op = []

for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    op.append((a, b, c))

C["".join(A)] = 0
q = [(0, "".join(A))]

while q:
    cost, s = heappop(q)

    if cost > C[s]:
        continue

    if check_order(s):
        print(cost)
        exit(0)

    sl = list(s)

    for a, b, c in op:
        sl[a], sl[b] = sl[b], sl[a]

        jsl = "".join(sl)

        if C.get(jsl, 1000) > c + cost:
            C[jsl] = c + cost
            heappush(q, (c + cost, jsl))

        sl[a], sl[b] = sl[b], sl[a]

print(-1)
