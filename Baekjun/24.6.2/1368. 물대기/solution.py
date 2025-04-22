import sys

input = sys.stdin.readline
MAX = float("inf")

N = int(input())
road_list = list()

for i in range(N):
    well_cost = int(input())
    road_list.append((well_cost, i + 1, 0))

for i in range(N):
    road_cost = list(map(int, input().split()))
    for j in range(i + 1, N):
        road_list.append((road_cost[j], i + 1, j + 1))

road_list.sort()
parent = list(range(N + 1))


def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]


def union(pa, pb):
    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb


answer, cnt = 0, N
for cost, a, b in road_list:
    if not cnt:
        break
    pa = find(a)
    pb = find(b)
    if pa != pb:
        cnt -= 1
        union(pa, pb)
        answer += cost

print(answer)
