from heapq import heappop, heappush


def solution():
    q = []

    N, M = map(int, input().split())
    MW = ["x"] + input().split()
    q = [(0, 1)]
    G = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)

    for _ in range(M):
        a, b, c = map(int, input().split())
        if MW[a] != MW[b]:
            G[a].append((b, c))
            G[b].append((a, c))
    ans = 0

    while q:
        c, n = heappop(q)

        if visited[n]:
            continue

        visited[n] = 1
        N -= 1
        ans += c

        if not N:
            break

        for next_node, cost in G[n]:
            if not visited[next_node]:
                heappush(q, (cost, next_node))

    if not N:
        print(ans)
    else:
        print(-1)


if __name__ == "__main__":
    solution()
