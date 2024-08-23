V = int(input())

parent = [i for i in range(V + 1)]
rank = [0 for _ in range(V + 1)]


def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


def union_by_rank(v1, v2):
    p1 = find(v1)
    p2 = find(v2)

    # rank가 큰 트리에 작은 트리를 붙입니다.
    if rank[p1] > rank[p2]:
        parent[p2] = p1
    elif rank[p1] < rank[p2]:
        parent[p1] = p2
    else:  # 만약 rank가 같다면 임의로 p1 트리에 p2 트리를 붙입니다.
        parent[p2] = p1
        rank[p1] += 1
