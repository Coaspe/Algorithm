import math
import sys


def dist(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)


input = sys.stdin.readline

N = int(input())
parent = [i for i in range(N+1)]
rank = [0 for _ in range(N+1)]
edges = []
points = []

for _ in range(N):
    points.append(tuple(map(float, input().split())))

for i in range(N):
    for j in range(i, N):
        edges.append((i, j, dist(points[i], points[j])))

edges.sort(key=lambda x: x[2])


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(p, c):
    p = find(p)
    c = find(c)

    if rank[p] > rank[c]:
        parent[c] = p
    elif rank[c] > rank[p]:
        parent[p] = c
    else:
        parent[c] = p
        rank[p] += 1


ans = 0
for a, b, c in edges:
    a = find(a)
    b = find(b)
    if a != b:
        union(a, b)
        ans += c
print("%0.2f" % ans)
