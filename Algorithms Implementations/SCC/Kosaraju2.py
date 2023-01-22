import sys
sys.setrecursionlimit(10 ** 6)

v, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(v + 1)]
reverse_graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    # 정방향 그래프 및 역방향 그래프에 주어진 그래프를 추가해준다.
    graph[a].append(b)
    reverse_graph[b].append(a)


# 정방향 dfs, dfs 가 종료되는 노드를 stack 에 쌓는다.
def dfs(node, visited, scc):
    visited[node] = 1
    for ne in graph[node]:
        if visited[ne] == 0:
            dfs(ne, visited, scc)
    scc.append(node)


# 역방향 dfs, 탐색하는 순서대로 stack (scc) 에 쌓는다.
def reverse_dfs(node, visited, scc):
    visited[node] = 1
    scc.append(node)
    for ne in reverse_graph[node]:
        if visited[ne] == 0:
            reverse_dfs(ne, visited, scc)


stack = []
visited = [0] * (v + 1)
# 모든 노드에서 정방향 dfs 를 수행한다.
for i in range(1, v + 1):
    if visited[i] == 0:
        dfs(i, visited, stack)
visited = [0] * (v + 1)
result = []

# 스택이 빌 때까지 pop 되는 요소에서 역방향 dfs 를 진행하여 scc 를 결과에 추가해준다.
while stack:
    ssc = []
    node = stack.pop()
    if visited[node] == 0:
        reverse_dfs(node, visited, ssc)
        result.append(sorted(ssc))

print(len(result))
results = sorted(result)
for i in results:
    print(*i, -1)
