import collections
N, M = map(int, input().split())
graph = collections.defaultdict(list)
indegree = [0] * (N+1)

for _ in range(M):
    o, i = map(int, input().split())
    graph[o].append(i)
    indegree[i] += 1

q = collections.deque([])

for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)
result = []
while q:
    i = q.popleft()
    result.append(i)

    for node in graph[i]:
        indegree[node] -= 1
        if indegree[node] == 0:
            q.append(node)

n = len(result)
for i in range(n):
    print(result[i], end=" " if i != n - 1 else "")
