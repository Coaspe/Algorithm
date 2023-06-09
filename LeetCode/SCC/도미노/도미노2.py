import sys
import collections
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    N, M = map(int, input().split())
    graph = collections.defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)

    stack = []
    low = [-1] * (N + 1)
    ids = [-1] * (N + 1)
    onStack = [0] * (N + 1)
    id = idx = 0

    def dfs(x):
        global id
        id += 1
        ids[x] = id
        low[x] = id

        onStack[x] = 1
        stack.append(x)

        for node in graph[x]:
            if ids[node] == -1:
                dfs(node)
                low[x] = min(low[x], low[node])
            elif onStack[node] == 1:
                low[x] = min(low[x], ids[node])

        w = -1
        if low[x] == ids[x]:
            global idx
            idx += 1
            while w != x:
                w = stack.pop()
                ids[w] = idx
                onStack[w] = 0

    for i in range(1, N + 1):
        if ids[i] == -1:
            dfs(i)

    scc_indegree = [0] * (1 + idx)

    for i in range(1, N + 1):
        for node in graph[i]:
            if ids[i] != ids[node]:
                scc_indegree[ids[node]] += 1
    answer = 0

    for i in range(1, len(scc_indegree)):
        if scc_indegree[i] == 0:
            answer += 1

    print(answer)
