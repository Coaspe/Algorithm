from collections import defaultdict
import heapq
import math
N, M = int(input()), int(input())
graph = defaultdict(list)
dp = [math.inf] * (N+1)
prev_node = [0] * (N+1)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
S, E = map(int, input().split())
dp[S] = 0

q = [(0, S)]

while q:
    cost, node = heapq.heappop(q)
    if cost > dp[node]:
        continue

    for nex, c in graph[node]:
        newCost = cost + c
        if dp[nex] > newCost:
            prev_node[nex] = node
            dp[nex] = newCost
            heapq.heappush(q, (newCost, nex))
print(dp[E])
arr = [E]
now = E
while now != S:
    now = prev_node[now]
    arr.append(now)
print(len(arr))
print(*arr[::-1])
