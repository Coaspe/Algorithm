from sys import stdin

input = stdin.readline
N = int(input())
A = list(map(int, input().split()))

G = [[] for _ in range(N)]

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append((b, c))
    G[b].append((a, c))
S, T = map(int, input().split())
S -= 1
T -= 1
from heapq import heappop, heappush

inf = -1
val = [[inf, 0] for _ in range(N)]
val[S] = [0, A[S]]
q = [(0, -A[S], S)]


while q:
    cost, water, node = heappop(q)

    water *= -1
    if (
        val[node][0] != inf
        and cost > val[node][0]
        or (cost == val[node][0] and water < val[node][1])
    ):
        continue

    val[node] = [cost, water]

    for next_node, next_cost in G[node]:
        new_cost = cost + next_cost
        new_water = water + A[next_node]

        if (
            val[next_node][0] == -1
            or val[next_node][0] > new_cost
            or (new_cost == val[next_node][0] and new_water > val[next_node][1])
        ):
            val[next_node] = [new_cost, new_water]
            heappush(q, (new_cost, -new_water, next_node))

if val[T][0] != inf:
    print(*val[T])
else:
    print(-1)
