def ripe(candid, count, graph, r, T):
    new_candid = set()
    for tomato in candid:
        r[tomato] = T
        count -= 1
        for to in graph[tomato]:
            if r[to] == -1 and to not in candid:
                new_candid.add(to)

    return new_candid, count


def main():
    N, M, K, Q = map(int, input().split())
    graph = [set() for _ in range(N+1)]
    r = [-1]*(N+1)
    T = 0

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)

    candid, _ = ripe(set(map(int, input().split())), 0, graph, r, T)

    for _ in range(Q):
        t, a, b = map(int, input().split())

        while t > T:
            T += 1
            candid, _ = ripe(candid, 0, graph, r, T)

        if a in graph[b]:
            graph[b].discard(a)
            graph[a].discard(b)

            if r[a] != -1 and b in candid and all(r[n] != -1 for n in graph[b]):
                candid.discard(b)

            if r[b] != -1 and a in candid and all(r[n] != -1 for n in graph[a]):
                candid.discard(a)
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
        candid, c = ripe(candid, count, graph, r, T)
        count = c

    print(*r[1:])


if __name__ == "__main__":
    main()
