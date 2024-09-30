from heapq import *
from collections import defaultdict

import sys

input = sys.stdin.readline

K, N, R = int(input()), int(input()), int(input())
edge_dict = defaultdict(list)

for _ in range(R):
    s, d, l, t = map(int, input().split())
    edge_dict[s - 1].append((d - 1, l, t))

MAX = float("inf")
dp = [[MAX] * (K + 1) for _ in range(N)]

dp[0][K] = 0
q = [(0, K, 0)]

answer = MAX

while q:
    dist, cost, node = heappop(q)

    if node == N - 1:
        answer = min(answer, dist)
        break

    for next_node, next_dist, next_cost in edge_dict[node]:
        new_cost = cost - next_cost
        new_dist = dist + next_dist
        if new_cost > -1 and dp[next_node][new_cost] > new_dist:
            dp[next_node][new_cost] = new_dist
            heappush(q, (new_dist, new_cost, next_node))

print(answer if answer < MAX else -1)
