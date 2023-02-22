import sys
from collections import deque
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, r, Q = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def cnt(node):
    count[node] = 1
    for i in graph[node]:
        if not count[i]:
            cnt(i)
            count[node] += count[i]


count = [0] * (n+1)
cnt(r)
for _ in range(Q):
    print(count[int(input())])
