import sys
import collections

n = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

# dx, dy : 방향배열(북, 남, 동, 서)
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

open_x, open_y = -1, -1
close_x, close_y = -1, -1

for i in range(n):
    for j in range(n):
        if arr[i][j] == '#':
            if open_x == -1 and open_y == -1:
                open_x, open_y = i, j
            else:
                close_x, close_y = i, j

check = [[[-1] * 4 for _ in range(n)] for _ in range(n)]
q = collections.deque()

for a in range(4):
    q.append((open_x, open_y, a))
    check[open_x][open_y][a] = 0

while q:
    x, y, dir = q.popleft()
    if x == close_x and y == close_y:
        print(check[x][y][dir])
        break
    nx, ny = x + dx[dir], y + dy[dir]

    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != '*':
        if check[nx][ny][dir] == -1 or check[nx][ny][dir] > check[x][y][dir]:
            check[nx][ny][dir] = check[x][y][dir]
            q.appendleft((nx, ny, dir))

        if arr[nx][ny] == '!':
            if dir < 2:
                for n_dir in range(2, 4):
                    if check[nx][ny][n_dir] == -1 or check[nx][ny][n_dir] > check[x][y][dir] + 1:
                        check[nx][ny][n_dir] = check[x][y][dir] + 1
                        q.append((nx, ny, n_dir))

            else:
                for n_dir in range(2):
                    if check[nx][ny][n_dir] == -1 or check[nx][ny][n_dir] > check[x][y][dir] + 1:
                        check[nx][ny][n_dir] = check[x][y][dir] + 1
                        q.append((nx, ny, n_dir))
