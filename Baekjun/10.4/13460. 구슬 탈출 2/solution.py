# BOJ 13460. 구슬 탈출 2


def solution():
    from sys import stdin
    from collections import deque

    input = stdin.readline

    N, M = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(N)]
    visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

    def move(x, y, dx, dy):
        cnt = 0
        while board[x + dx][y + dy] != "#" and board[x][y] != "O":
            x += dx
            y += dy
            cnt += 1
        return x, y, cnt

    def bfs(rx, ry, bx, by):
        q = deque([(rx, ry, bx, by, 1)])
        visited[rx][ry][bx][by] = True

        while q:
            rx, ry, bx, by, depth = q.popleft()
            if depth > 10:
                break

            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                nrx, nry, rcnt = move(rx, ry, dx, dy)
                nbx, nby, bcnt = move(bx, by, dx, dy)

                if board[nbx][nby] == "O":
                    continue

                if board[nrx][nry] == "O":
                    print(depth)
                    return

                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= dx
                        nry -= dy
                    else:
                        nbx -= dx
                        nby -= dy

                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    q.append((nrx, nry, nbx, nby, depth + 1))

        print(-1)

    for i in range(N):
        for j in range(M):
            if board[i][j] == "R":
                rx, ry = i, j
            elif board[i][j] == "B":
                bx, by = i, j

    bfs(rx, ry, bx, by)


if __name__ == "__main__":
    solution()
