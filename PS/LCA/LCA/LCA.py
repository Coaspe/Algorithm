import sys
import collections
input = sys.stdin.readline  # 시간 초과를 피하기 위한 빠른 입력 함수
sys.setrecursionlimit(int(1e5))  # 런타임 오류를 피하기 위한 재귀 깊이 제한 설정
LOG = 21  # 2^20 = 1,000,000

T = int(input())

for _ in range(T):
    n = int(input())
    root = -1
    parent = [[0] * LOG for _ in range(n+1)]  # 부모 노드 정보
    d = [0] * (n+1)  # 각 노드까지의 깊이
    c = [False] * (n+1)  # 각 노드의 깊이가 계산되었는지 여부
    graph = collections.defaultdict(list)

    for _ in range(n-1):
        a, b = map(int, input().split())
        if root == -1 or b == root:
            root = a
        graph[a].append(b)
        graph[b].append(a)

    # Set depth
    def dfs(node, depth):
        c[node] = True
        d[node] = depth
        for child in graph[node]:
            if not c[child]:
                parent[child][0] = node
                dfs(child, depth+1)

    def set_parent():
        global root
        dfs(root, 0)
        for i in range(1, LOG):
            for j in range(1, n+1):
                parent[j][i] = parent[parent[j][i-1]][i-1]

    def lca(a, b):
        if d[a] > d[b]:
            a, b = b, a

        for i in range(LOG-1, -1, -1):
            if d[b] - d[a] >= (1 << i):
                b = parent[b][i]

        if a == b:
            return a

        for i in range(LOG-1, -1, -1):
            if parent[a][i] != parent[b][i]:
                a = parent[a][i]
                b = parent[b][i]

        return parent[a][0]

    set_parent()
    a, b = map(int, input().split())
    print(lca(a, b))
