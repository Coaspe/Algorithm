from sys import stdin


input = stdin.readline
N, Q = map(int, input().split())
P = [-1] * (N + 1)
PP = [i for i in range(N + 1)]
P[1] = 1
for idx in range(N - 1):
    P[idx + 2] = int(input())


def find(c):
    stack = []
    while PP[c] != c:
        stack.append(c)
        c = PP[c]

    while stack:
        PP[stack.pop()] = c
    return c


def union(c1, c2):
    p1, p2 = find(c1), find(c2)
    if p1 == p2:
        return
    if p1 > p2:
        PP[p1] = p2
    else:
        PP[p2] = p1


query = [tuple(map(int, input().split())) for _ in range(Q + N - 1)]

C = set()
for i, v in enumerate(query):
    if v[0] == 1:
        continue
    C.add(v[1])

for i in range(2, N + 1):
    if i in C:
        continue

    union(i, P[i])

ans = []
while query:
    qq = query.pop()

    if qq[0] == 0:
        union(qq[1], P[qq[1]])
    else:
        if find(qq[1]) == find(qq[2]):
            ans.append("YES")
        else:
            ans.append("NO")

print("\n".join(reversed(ans)))
