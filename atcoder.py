from collections import deque
d = deque()
N, M = map(int, input().split())
A = []
for i in range(N):
    s = input()
    A.append(s)

V = [[[0]*5 for _ in range(M)] for _ in range(N)]

d.append((1, 1, 4))

V[1][1][4] = 1

E = [(0, 1), (0, -1), (1, 0), (-1, 0)]

while d:
    y, x, dd = d.popleft()
    if dd != 4:
        ny, nx = y+E[dd][0], x+E[dd][1]
        if A[ny][nx] == '.' and V[ny][nx][dd] == 0:
            V[ny][nx][dd] = 1
            d.append((ny, nx, dd))
        elif A[ny][nx] == '#' and V[y][x][4] == 0:
            V[y][x][4] = 1
            d.append((y, x, 4))

    else:
        for i in range(4):
            dy, dx = E[i]
            ny, nx, dd = y+dy, x+dx, i
            if V[ny][nx][i] == 0 and A[ny][nx] == '.':
                V[ny][nx][i] = 1
                d.append((ny, nx, i))

ans = 0
for i in range(N):
    for j in range(M):
        ans += max(V[i][j])
print(ans)
