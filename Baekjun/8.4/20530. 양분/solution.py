import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000000)


def find_cycle(cur, prev):
    for i in L[cur]:
        if i == prev:
            continue
        if not visited[i]:
            visited[i] = 1
            parent[i] = cur
            k = find_cycle(i, cur)
            if k:
                return k
        else:
            return [i, cur]

    return 0


def set_group(target, cycle_node):
    for i in L[target]:
        if not cycle[i] and not visited[i]:
            parent[i] = cycle_node
            visited[i] = 1
            set_group(i, cycle_node)


n, q = map(int, input().split())

parent = [i for i in range(n + 1)]
L = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
cycle = [0 for _ in range(n + 1)]

for i in range(n):
    a, b = map(int, input().split())
    L[a].append(b)
    L[b].append(a)

visited[1] = 1
a, b = find_cycle(1, 0)

while a != b:
    cycle[b] = 1
    b = parent[b]
cycle[a] = 1

visited = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    if cycle[i]:
        visited[i] = 1
        parent[i] = i
        set_group(i, i)

for i in range(q):
    a, b = map(int, input().split())
    if parent[a] == parent[b]:
        print(1)
    else:
        print(2)
