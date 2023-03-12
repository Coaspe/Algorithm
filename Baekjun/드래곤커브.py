N = int(input())
board = [[0]*101 for _ in range(101)]

dx = (0, -1, 0, 1)
dy = (1, 0, -1, 0)

for _ in range(N):
    y, x, d, g = map(int, input().split())
    total_array = [(x, y), (x+dx[d], y+dy[d])]
    board[x][y] = 1
    board[x+dx[d]][y+dy[d]] = 1
    for generation in range(g):
        add_array = []
        lx, ly = total_array[-1][0], total_array[-1][1]
        for px, py in total_array[len(total_array)-2::-1]:
            nx = lx - (ly - py)
            ny = ly + (lx - px)
            if not (0 <= nx <= 100 and 0 <= ny <= 100):
                break
            board[nx][ny] = 1
            add_array.append((nx, ny))
        total_array.extend(add_array)
        add_array.clear()
cnt = 0
for i in range(100):
    for j in range(100):
        if not (board[i][j] == 1):
            continue
        if not (board[i][j+1] == 1):
            continue
        if not (board[i+1][j] == 1):
            continue
        if board[i+1][j+1] == 1:
            cnt = cnt + 1
print(cnt)
