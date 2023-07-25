import heapq
N = int(input())
R = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(R):
    a, b, c = map(int, input().split())
    graph[a].append((-c, b))

start, dest = map(int, input().split())
# (cost, num of city)
dist = [(0, 0)] * (N+1)
q = [(0, 0, start)]

ans_cost, ans_num = 0, 0

while q:
    cost, noc, node = heapq.heappop(q)

    if cost > dist[node][0]:
        continue

    for next_cost, next_node in graph[node]:
        new_cost = cost + next_cost

        if dist[next_node][0] > new_cost:
            dist[next_node] = (new_cost, noc - 1)
            heapq.heappush(q, (new_cost, noc - 1, next_node))

print(dist[dest])
