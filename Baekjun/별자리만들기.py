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


def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


def union_by_rank(p1, p2):
    if rank[p1] > rank[p2]:
        parent[p2] = p1
    elif rank[p1] < rank[p2]:
        parent[p1] = p2
    else:
        parent[p2] = p1
        rank[p1] += 1


answer = 0
for s, e, w in edges:
    p1 = find(s)
    p2 = find(e)
    if p1 != p2:
        union_by_rank(p1, p2)
        answer += w
print("%0.2f" % answer)
