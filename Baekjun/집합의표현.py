n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
rank = [0 for _ in range(n + 1)]


def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


def union_by_rank(v1, v2):
    p1 = find(v1)
    p2 = find(v2)

    if rank[p1] > rank[p2]:
        parent[p2] = p1
    elif rank[p1] < rank[p2]:
        parent[p1] = p2
    else:
        parent[p2] = p1
        rank[p1] += 1


def find(a):
    while a != parent[a]:
        a = parent[a]
    return a


def union(p, c):
    p = find(p)
    c = find(c)

    parent[c] = p


for _ in range(m):
    op, a, b = map(int, input().split())

    if op:
        print("YES" if find(a) == find(b) else "NO")
    else:
        union(a, b)
