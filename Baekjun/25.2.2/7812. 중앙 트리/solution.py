from sys import stdin, setrecursionlimit
from collections import deque

setrecursionlimit(10**5)
input = stdin.readline
while True:
    N = int(input())
    if N == 0:
        break

    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b, w = map(int, input().split())
        G[a].append((b, w))
        G[b].append((a, w))

    root = 0
    parent = [-1] * N
    children = [[] for _ in range(N)]
    q = deque()
    q.append(root)

    while q:
        u = q.popleft()
        for v, w in G[u]:
            if parent[v] == -1 and v != parent[u]:
                parent[v] = u
                children[u].append((v, w))
                q.append(v)

    num_of_children = [0] * N

    def set_num_of_children(node):
        num_of_children[node] = 1
        for child, _ in children[node]:
            num_of_children[node] += set_num_of_children(child)
        return num_of_children[node]

    set_num_of_children(root)

    def get_root_cost(node, edge_cost):
        if not children[node]:
            return edge_cost

        cost = 0

        for child, child_cost in children[node]:
            cost += get_root_cost(child, child_cost)

        return cost + edge_cost * (num_of_children[node])

    min_cost = get_root_cost(root, 0)

    def get_min_cost(prev_cost, edge_cost, node):
        global min_cost
        prev_cost = (
            prev_cost
            - edge_cost * num_of_children[node]
            + edge_cost * (N - num_of_children[node])
        )
        min_cost = min(min_cost, prev_cost)

        for child, child_cost in children[node]:
            get_min_cost(
                prev_cost,
                child_cost,
                child,
            )

    for child, child_cost in children[root]:
        get_min_cost(min_cost, child_cost, child)

    print(min_cost)
