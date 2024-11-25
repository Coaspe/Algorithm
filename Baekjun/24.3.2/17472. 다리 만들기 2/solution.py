N, M = map(int, input().split())
CC = [list(map(int, input().split())) for _ in range(N)]
C = [c[:] for c in CC]


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def find_island(x, y):
    C[x][y] = len(islands)
    CC[x][y] = 0
    islands[-1].add((x, y))

    for i in range(4):
        row, col = x + dx[i], y + dy[i]
        if 0 <= row < N and 0 <= col < M and CC[row][col]:
            find_island(row, col)


islands = []
for n in range(N):
    for m in range(M):
        if CC[n][m]:
            islands.append(set())
            find_island(n, m)

G = [set() for _ in range(len(islands) + 1)]

# 오 왼 위 아래


def find_path(x, y):
    for i in range(4):
        row, col = x, y
        flag = False
        for _ in range(2):
            row += dx[i]
            col += dy[i]

            if not (0 <= row < N) or not (0 <= col < M) or C[row][col] != 0:
                flag = True
                break
        if flag:
            continue

        dist = 2
        while 0 <= row < N and 0 <= col < M and C[row][col] == 0:
            dist += int(C[row][col] == 0)
            row += dx[i]
            col += dy[i]

        if 0 <= row < N and 0 <= col < M and C[row][col] != C[x][y]:
            G[C[x][y]].add((C[row][col], dist - 1))
            G[C[row][col]].add((C[x][y], dist - 1))


for i in islands:
    for x, y in i:
        find_path(x, y)

import heapq


n = len(islands)

heap = [(0, 1)]

in_mst = [False] * (n + 1)

mst_cost = 0
edges_used = 0

while edges_used < n and heap:
    weight, curr_node = heapq.heappop(heap)

    if in_mst[curr_node]:
        continue

    in_mst[curr_node] = True
    mst_cost += weight
    edges_used += 1

    for next_node, new_weight in G[curr_node]:
        if not in_mst[next_node]:
            heapq.heappush(heap, (new_weight, next_node))

if all(in_mst[1:]):
    print(mst_cost)
else:
    print(-1)
