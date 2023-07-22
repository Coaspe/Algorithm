
N, M, K, Q = map(int, input().split())
T = 0
graph = [set() for _ in range(N+1)]
r = [-1]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)


def check(node):
    for n in graph[node]:
        if r[n] != -1:
            return False
    return True


def ripe(candid, count):
    new_candid = set()
    for tomato in candid:
        r[tomato] = T
        count -= 1
        for to in graph[tomato]:
            if r[to] == -1 and to not in candid:
                new_candid.add(to)

    return new_candid, count


candid, _ = ripe(set(map(int, input().split())), 0)

for _ in range(Q):
    t, a, b = map(int, input().split())

    while t > T:
        T += 1
        candid, _ = ripe(candid, 0)

    # 이미 이어져 있음 -> 삭제
    if a in graph[b]:
        graph[b].remove(a)
        graph[a].remove(b)

        if r[a] != -1 and b in candid and check(b):
            candid.remove(b)
        if r[b] != -1 and a in candid and check(a):
            candid.remove(a)
    # 이어져있지 않음 -> 연결
    else:
        graph[b].add(a)
        graph[a].add(b)

        if (r[b] == -1) != (r[a] == -1):
            c = a if r[a] == -1 else b
            candid.add(c)

parent = [i for i in range(N + 1)]


def find(v):
    root = v
    while parent[root] != root:
        root = parent[root]

    # Path Compression
    while v != root:
        parent[v], v = root, parent[v]

    return root


def union_by_rank(v1, v2):
    p1 = find(v1)
    p2 = find(v2)

    if p1 != p2:
        if r[p1] != -1:
            parent[p2] = p1
        elif r[p2] != -1:
            parent[p1] = p2
        else:
            parent[p2] = p1


for i in range(1, N+1):
    for n in graph[i]:
        union_by_rank(i, n)

count = 0

for i in range(1, N+1):
    if r[i] == -1 and r[find(i)] > -1:
        count += 1

while count:
    T += 1
    candid, c = ripe(candid, count)
    count = c

print(*r[1:])
