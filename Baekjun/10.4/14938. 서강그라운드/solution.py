from heapq import heappush, heappop


def solution():
    N, M, R = map(int, input().split())
    items = list(map(int, input().split()))
    G = [[] for _ in range(N)]

    for _ in range(R):
        u, v, w = map(int, input().split())
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))

    def dijkstra(s):
        dist = [float("inf")] * N
        dist[s] = 0
        heap = [(0, s)]

        while heap:
            d, u = heappop(heap)
            if d > dist[u]:
                continue
            for v, w in G[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heappush(heap, (dist[v], v))

        return dist

    ans = 0

    for i in range(N):
        tmp_ans = 0
        dist = dijkstra(i)
        for j in range(N):
            if dist[j] <= M:
                tmp_ans += items[j]
        ans = max(ans, tmp_ans)

    print(ans)


if __name__ == "__main__":
    solution()
