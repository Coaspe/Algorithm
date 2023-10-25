from sys import stdin

input = stdin.readline

N, M = map(int, input().split())

parent = [i for i in range(N)]
rank = [0 for _ in range(N)]


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


for i in range(M):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print(i + 1)
        break
    else:
        union_by_rank(a, b)
else:
    print(0)
