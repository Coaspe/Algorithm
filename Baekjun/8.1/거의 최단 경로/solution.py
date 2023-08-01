import math
import heapq


def solution():
    N = M = S = E = graph = not_allowed_paths = None

    def dijk():
        dist = [[math.inf, []]] * N
        dist[S] = [0, [f'{S}']]
        q = [(0, f'{S}')]

        while q:
            cost, path = heapq.heappop(q)
            node = int(path[-1])

            if cost > dist[node][0]:
                continue

            for next_node, next_cost in graph[node]:
                new_cost = cost + next_cost
                new_path = path + f'{next_node}'

                if dist[next_cost][0] > new_cost:
                    dist[next_cost] = [new_cost, [new_path]]
                    heapq.heappush(q, [new_cost, new_path])
                elif dist[next_cost][0] == cost:
                    dist[next_cost][1].append(new_path)
                    heapq.heappush(q, [new_cost, new_path])

        return dist[E][1]

    while True:
        N, M = map(int, input().split())

        if N == M == 0:
            return

        S, E = map(int, input().split())

        graph = [[] for _ in range(N)]
        not_allowed_paths = [[0] * N for _ in range(N)]

        for _ in range(M):
            u, v, p = map(int, input().split())
            graph[u].append((v, p))

        paths = dijk()
        print(paths)
        for path in paths:
            path = map(int, list(path))
            for idx in range(1, len(path)):
                not_allowed_paths[path[idx - 1]][path[idx]] = 1


solution()
