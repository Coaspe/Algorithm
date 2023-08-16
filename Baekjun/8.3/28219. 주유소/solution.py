N, k = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

stack = [1]
visited = [0] * (N + 1)
dist = [0] * (N + 1)
ans = 0

while stack:
    node = stack[-1]
    if not visited[node]:
        visited[node] = 1
        for neigh in graph[node]:
            if not visited[neigh]:
                stack.append(neigh)
        continue

    visited[node] = 2

    dist1 = dist2 = 0
    for neigh in graph[node]:
        if visited[neigh] == 2:
            if dist1 <= dist[neigh]:
                dist2 = dist1
                dist1 = dist[neigh]
            elif dist2 <= dist[neigh]:
                dist2 = dist[neigh]

    if k <= dist1 + dist2:
        dist[node] = 0
        ans += 1
    else:
        dist[node] = dist1 + 1

    stack.pop()

print(ans)
