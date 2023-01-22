import sys
sys.setrecursionlimit(10 ** 6)

v, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

stack = []
low = [-1] * (v + 1)
ids = [-1] * (v + 1)
onStack = [0] * (v + 1)
id = 0
result = []


def dfs(x):
    global id
    ids[x] = low[x] = id
    id += 1
    onStack[x] = 1
    stack.append(x)

    for node in graph[x]:
        if ids[node] == -1:
            dfs(node)
            low[x] = min(low[x], low[node])
        elif onStack[node] == 1:
            low[x] = min(low[x], ids[node])

    w = -1
    scc = []
    if low[x] == ids[x]:
        while w != x:
            w = stack.pop()
            scc.append(w)
            onStack[w] = -1
        result.append(sorted(scc))


for i in range(1, v + 1):
    if ids[i] == -1:
        dfs(i)

print(len(result))
for i in sorted(result):
    print(*i, -1)
