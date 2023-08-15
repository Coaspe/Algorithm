import sys

n = int(input())

input = sys.stdin.readline
graph = []
degree = [0] * n
visit = [[0] * n for _ in range(n)]

for i in range(n):
    lst = {}

    for j, v in enumerate(list(map(int, input().split()))):
        if v:
            lst[j] = 1
            visit[i][j] = v
            degree[i] += v

    graph.append(lst)

for i in range(n):
    if degree[i] % 2:
        print(-1)
        sys.exit()

answer = []
stack = [0]

while stack:
    current = stack[-1]

    if graph[current]:
        _next = next(iter(graph[current]))
        visit[_next][current] -= 1
        visit[current][_next] -= 1
        degree[current] -= 1
        degree[_next] -= 1

        if not visit[current][_next]:
            del graph[current][_next]
            del graph[_next][current]

        stack.append(_next)
    else:
        answer.append(stack.pop() + 1)

for i in range(n):
    if degree[i]:
        print(-1)
        sys.exit()

print(" ".join(map(str, answer)))
