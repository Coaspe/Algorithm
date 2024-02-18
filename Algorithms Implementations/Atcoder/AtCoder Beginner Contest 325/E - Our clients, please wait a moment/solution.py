from heapq import heappop, heappush
from sys import stdin

input = stdin.readline
INF = float("inf")
N, A, B, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(N)]


def dijkstra(start, weight1, weight2):
    dist = [INF] * N
    done = [False] * N
    dist[start] = 0
    hq = list()

    heappush(hq, [0, start])

    while hq:
        now_dist, now_node = heappop(hq)

        if done[now_node] == True:
            continue

        done[now_node] = True

        for to_node in range(N):
            if done[to_node] == False:
                to_dist = now_dist + D[now_node][to_node] * weight1 + weight2
                if dist[to_node] > to_dist:
                    dist[to_node] = to_dist
                    heappush(hq, [to_dist, to_node])

    return dist


ans = INF
d1 = dijkstra(0, A, 0)
d2 = dijkstra(N - 1, B, C)

for i in range(N):
    ans = min(ans, d1[i] + d2[i])

print(ans)
