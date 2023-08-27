from collections import deque
import sys

# 재귀깊이해제
sys.setrecursionlimit(300000)
N, Q = map(int, input().split())

graph = [[] for _ in range(N)]
for _ in range(N):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

check = [0] * N
parent = [i for i in range(N)]
fin = [0] * N
is_cycle = set()


def go(cur, base):
    is_cycle.add(base)
    while cur != base:
        is_cycle.add(cur)
        cur = parent[cur]


# prev is parent
def dfs(cur, prev):
    check[cur] = 1
    for i in graph[cur]:
        if i == prev:
            continue

        if not check[i]:
            parent[i] = cur
            if dfs(i, cur):
                return True

        elif not fin[i]:
            go(cur, i)
            return True

    fin[cur] = True
    return False


tree_num = [0] * N


def set_tree_group(cycle_node, num):
    q = deque([cycle_node])
    c = [0] * N

    while q:
        n = q.popleft()

        if n != cycle_node and n in is_cycle:
            continue

        tree_num[n] = num

        for i in graph[n]:
            if not c[i]:
                q.append(i)
                c[i] = 1


dfs(0, -1)

for idx, cycle_node in enumerate(is_cycle):
    set_tree_group(cycle_node, idx + 1)

for _ in range(Q):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if (u in is_cycle and v in is_cycle) or tree_num[u] == tree_num[v]:
        print(1)
    else:
        print(2)

##

import sys
from collections import deque
import heapq
import bisect
import math
from itertools import product
from itertools import combinations

input = sys.stdin.readline
sys.setrecursionlimit(100000000)


def find_cycle(x, y):
    for i in L[x]:
        if i != y:
            if not visited[i]:
                visited[i] = 1
                parent[i] = x
                k = find_cycle(i, x)
                if k:
                    return k
            else:
                return [i, x]
    return 0


def dfs(x, y):
    for i in L[x]:
        if not cycle[i] and not visited[i]:
            visited[i] = 1
            parent[i] = y
            dfs(i, y)


n, q = map(int, input().split())

parent = [i for i in range(n + 1)]
L = [[] for _ in range(n + 1)]
visited = [0 for i in range(n + 1)]
cycle = [0 for i in range(n + 1)]

for i in range(n):
    a, b = map(int, input().split())
    L[a].append(b)
    L[b].append(a)

visited = [0 for i in range(n + 1)]
visited[1] = 1
a, b = find_cycle(1, 0)

while a != b:
    cycle[b] = 1
    b = parent[b]
cycle[a] = 1

visited = [0 for i in range(n + 1)]
for i in range(1, n + 1):
    if cycle[i]:
        visited[i] = 1
        parent[i] = i
        dfs(i, i)

for i in range(q):
    a, b = map(int, input().split())
    if parent[a] == parent[b]:
        print(1)
    else:
        print(2)

###

import sys

input = lambda: map(int, sys.stdin.readline().split())
N, Q = input()
graph = [[] for _ in range(N + 1)]
degree = [0 for _ in range(N + 1)]

for _ in range(N):
    a, b = input()
    degree[a] += 1
    degree[b] += 1
    graph[a].append(b)
    graph[b].append(a)

visited = [-1 for _ in range(N + 1)]
q = [i for i, v in enumerate(degree) if v == 1]

while q:
    nq = []
    for cur in q:
        for nxt in graph[cur]:
            if visited[nxt] == -1:
                visited[cur] = nxt
                degree[nxt] -= 1
                if degree[nxt] == 1:
                    nq.append(nxt)
    q = nq


def zp(x):
    if visited[x] == x:
        return x

    if visited[x] == -1:
        visited[x] = x
        return x

    visited[x] = zp(visited[x])
    return visited[x]


for i in range(1, N + 1):
    zp(i)

ans = []
for _ in range(Q):
    u, v = input()
    ans.append(
        "1"
        if visited[u] == visited[v]
        or (visited[u] == -1 and visited[v] == u)
        or (visited[v] == -1 and visited[u] == v)
        else "2"
    )

print("\n".join(ans))
