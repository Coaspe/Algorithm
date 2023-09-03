from collections import defaultdict

N, P = map(int, input().split())

graph = defaultdict(list)

for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
# 최대한 많은 경로. 경로가 겹치면 안 된다.
