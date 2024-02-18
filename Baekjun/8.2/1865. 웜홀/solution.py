from sys import maxsize

T = int(input())


def bf():
    graph = []
    dist = [maxsize] * (N + 1)
    dist[1] = 0

    for _ in range(M):
        a, b, c = map(int, input().split())
        graph.append((a, b, c))
        graph.append((b, a, c))

    for _ in range(W):
        a, b, c = map(int, input().split())
        graph.append((a, b, -c))

    for i in range(N):
        for s, e, c in graph:
            if dist[e] > dist[s] + c:
                dist[e] = dist[s] + c

                if i == N - 1:
                    print("YES")
                    return

    print("NO")


while T:
    T -= 1
    N, M, W = map(int, input().split())

    bf()
