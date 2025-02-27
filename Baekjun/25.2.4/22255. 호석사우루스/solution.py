from heapq import heappop, heappush

N, M = map(int, input().split())
Sx, Sy, Ex, Ey = map(int, input().split())

Sx -= 1
Sy -= 1
Ex -= 1
Ey -= 1

R = [list(map(int, input().split())) for _ in range(N)]

q = [(0, 1, Sx, Sy)]

distance = [[[float("inf")] * 3 for _ in range(M)] for _ in range(N)]

distance[Sx][Sy][1] = 0

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

while q:
    t, n, x, y = heappop(q)

    if t > distance[x][y][n]:
        continue

    new_n = n + 1
    new_n %= 3

    for i in range(4):
        if n == 1 and i <= 1:
            continue
        if n == 2 and i > 1:
            break

        xx, yy = x + dx[i], y + dy[i]

        if 0 <= xx < N and 0 <= yy < M:
            if R[xx][yy] == -1:
                continue

            new_dist = t + R[xx][yy]

            if new_dist >= distance[xx][yy][new_n]:
                continue

            distance[xx][yy][new_n] = new_dist
            heappush(q, (new_dist, new_n, xx, yy))

ans = min(distance[Ex][Ey])

print(ans if ans != float("inf") else -1)
