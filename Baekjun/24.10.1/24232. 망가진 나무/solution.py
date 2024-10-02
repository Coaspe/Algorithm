import sys

input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
order = dict()
edges = ["0"] * (N - 1)
for i in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append((v, 1, i))
    graph[v].append((u, 0, i))


def dfs():
    S = [1]
    MAX = 10**6
    visited = [MAX] * (N + 1)
    visited[1] = 0

    goal = 1

    while S:
        now = S.pop()

        for node, f, i in graph[now]:
            if visited[node] != MAX:
                continue

            if f == 0:
                visited[node] = visited[now] - 1
            else:
                visited[node] = visited[now] + 1

            if visited[node] < visited[goal]:
                goal = node
            S.append(node)
    return goal


goal = dfs()


def dfs2():
    V = [0] * (N + 1)
    V[goal] = 1
    S = [goal]

    while S:
        n = S.pop()
        for node, f, i in graph[n]:
            if V[node]:
                continue

            V[node] = 1
            if f == 0:
                edges[i] = "1"

            S.append(node)


dfs2()

print("".join(edges))
