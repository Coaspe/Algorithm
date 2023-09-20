from collections import deque

N = int(input())

time = [0] * (N + 1)
ans = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
outdegree = [0] * (N + 1)
q = deque()

for i in range(1, N + 1):
    x = list(map(int, input().split()))[:-1]
    time[i] = x[0]

    # i를 짓는 데 j가 필요함
    for j in x[1:]:
        graph[j].append(i)
        outdegree[i] += 1

for i in range(1, N + 1):
    if not outdegree[i]:
        q.append(i)
        ans[i] = time[i]

while q:
    building = q.popleft()

    for d in graph[building]:
        outdegree[d] -= 1
        ans[d] = max(ans[d], time[d] + ans[building])

        if outdegree[d] == 0:
            q.append(d)

print(*ans[1:], sep="\n")
