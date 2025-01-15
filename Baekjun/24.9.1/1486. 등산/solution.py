from collections import defaultdict, deque

N, M, Q = map(int, input().split())


G = [[] for _ in range(N)]
P = [i for i in range(N)]


def find(c):
    if P[c] != c:
        P[c] = find(P[c])
    return P[c]


def union(c1, c2):
    p1, p2 = find(c1), find(c2)

    if p1 > p2:
        P[p2] = p1
    else:
        P[p1] = p2


cache = defaultdict(int)

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
    union(a, b)


def bfs(s, e):
    if tuple(sorted([s, e])) in cache:
        return cache[tuple(sorted([s, e]))]

    C = set()

    q = deque([(s, 0)])

    while q:
        node, cnt = q.popleft()

        if node == e:
            return cnt

        for next_node in G[node]:
            if next_node not in C:
                C.add(next_node)
                q.append((next_node, cnt + 1))

    return 1


for _ in range(Q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    if a == b:
        print(0)
        continue

    if find(a) != find(b):
        print(1)
        continue

    print(bfs(a, b))
print(cache)
