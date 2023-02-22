import sys
import heapq


def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, [0, start])

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for x in graph[now]:
            cost = dist + x[1]
            if distance[x[0]] > cost:
                heapq.heappush(q, [cost, x[0]])
                distance[x[0]] = cost
                check[x[0]] = check[now]
                if (g == now and h == x[0]) or (h == now and g == x[0]):
                    check[x[0]] = 1

            elif distance[x[0]] == cost:
                check[x[0]] = max(check[x[0]], check[now])
                if (g == now and h == x[0]) or (h == now and g == x[0]):
                    check[x[0]] = 1


input = sys.stdin.readline
for tc in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append([b, d])
        graph[b].append([a, d])

    departure = []
    for _ in range(t):
        departure.append(int(input()))
    departure.sort()

    INF = int(1e9)
    distance = [INF for _ in range(n+1)]
    check = [0 for _ in range(n+1)]
    dijkstra(s)
    for x in departure:
        if check[x]:
            print(x, end=' ')
    print()
