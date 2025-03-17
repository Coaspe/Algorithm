from collections import deque


def solution(n, edges):
    adj = [[] for _ in range(n + 1)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    def bfs(start):
        dist = [-1] * (n + 1)
        dist[start] = 0
        queue = deque([start])
        far_node = start
        while queue:
            cur = queue.popleft()
            for nxt in adj[cur]:
                if dist[nxt] == -1:
                    dist[nxt] = dist[cur] + 1
                    queue.append(nxt)
                    if dist[nxt] > dist[far_node]:
                        far_node = nxt
        return far_node, dist

    u, _ = bfs(1)

    v, dist_u = bfs(u)
    D = dist_u[v]

    count_d_u = sum(1 for x in dist_u if x == D)
    if count_d_u >= 2:
        return D

    w, dist_v = bfs(v)
    count_d_v = sum(1 for x in dist_v if x == D)
    if count_d_v >= 2:
        return D
    else:
        return D - 1
