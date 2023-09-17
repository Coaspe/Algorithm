from collections import deque, defaultdict
import sys

input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
dic = defaultdict(int)
max_c = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    x = (min(a, b), max(a, b))
    max_c = max(max_c, c)
    dic[x] = max(dic[x], c)

for (a, b), val in dic.items():
    graph[a].append((b, val))
    graph[b].append((a, val))

A, B = map(int, input().split())


def bfs(mid):
    q = deque([A])
    check = [0] * (N + 1)
    check[A] = 1

    while q:
        node = q.popleft()

        if node == B:
            return True

        for next_node, new_cost in graph[node]:
            if not check[next_node] and new_cost >= mid:
                check[next_node] = 1
                q.append(next_node)

    return False


s, e = 0, max_c + 1
result = 0

while e > s + 1:
    mid = (s + e) // 2

    if bfs(mid):
        result = max(result, mid)
        s = mid
    else:
        e = mid

print(int(result))
