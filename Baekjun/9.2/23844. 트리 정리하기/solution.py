from sys import stdin, setrecursionlimit

read = stdin.readline
setrecursionlimit(100000)  # recursion error 방지


def dfs(node: int, level: int):
    # 남길 수 있는 노드 K 보다 작은 경우
    # 만약 K 이상이 되는 순간 카운트는 하지 않는다.
    if level_count[level] < limit_count:
        level_count[level] += 1
    else:
        print(node - 1)

    for child_node in graph_list[node]:
        if not visited[child_node]:
            visited[child_node] = True
            dfs(child_node, level + 1)


node_count, limit_count = map(int, read().split())
graph_list = [[] for _ in range(node_count + 1)]  # 1부터 노드 개수까지의 번호가 있음.
level_count = [0] * node_count  # 최대 레벨만큼 0으로 초기화
visited = [False] * (node_count + 1)  # 방문 노드 처리

# n-1만큼 입력을 받음
for _ in range(node_count - 1):
    # 두 노드를 입력받고 각 노드별 연결노드 리스트에 추가한다.
    node1, node2 = map(int, read().split())
    graph_list[node1 + 1].append(node2 + 1)
    graph_list[node2 + 1].append(node1 + 1)

# == DFS ==
visited[1] = True
dfs(1, 0)

print(sum(level_count))
