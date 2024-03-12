from collections import deque
from sys import stdin

input = stdin.readline


def solution():
    N = int(input())

    B = [input() for _ in range(N)]

    check = [[[0] * 2 for _ in range(N)] for _ in range(N)]

    C = D = None

    for i in range(N):
        for j in range(N):
            if B[i][j] == "B":
                if i + 1 < N and B[i + 1][j] == "B":
                    C = (i + 1, j)
                    D = 1
                elif j + 1 < N and B[i][j + 1] == "B":
                    C = (i, j + 1)
                    D = 0
                break

        if C:
            break

    check[C[0]][C[1]][D] = 1

    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    dxx, dyy = [0, 0, 1, 1, 1, -1, -1, -1], [1, -1, -1, 0, 1, -1, 0, 1]
    q = deque([(C[0], C[1], D, 0)])

    def check_rotation(r, c):

        for i in range(8):
            row, col = r + dxx[i], c + dyy[i]

            if not (0 <= row < N) or not (0 <= col < N) or B[row][col] == "1":
                return False

        return True

    while q:
        r, c, d, cost = q.popleft()

        if (d and B[r - 1][c] == B[r][c] == B[r + 1][c] == "E") or (
            not d and B[r][c - 1] == B[r][c] == B[r][c + 1] == "E"
        ):
            print(cost)
            return

        for i in range(4):
            row, col = r + dx[i], c + dy[i]

            if 0 <= row < N and 0 <= col < N:
                if (
                    d
                    and 1 <= row < N - 1
                    and B[row - 1][col] != "1"
                    and B[row][col] != "1"
                    and B[row + 1][col] != "1"
                    and not check[row][col][d]
                ) or (
                    not d
                    and 1 <= col < N - 1
                    and B[row][col - 1] != "1"
                    and B[row][col] != "1"
                    and B[row][col + 1] != "1"
                    and not check[row][col][d]
                ):
                    check[row][col][d] = 1
                    q.append((row, col, d, cost + 1))

        if check_rotation(r, c) and not check[r][c][(abs(d - 1))]:
            check[r][c][abs(d - 1)] = 1
            q.append((r, c, abs(d - 1), cost + 1))

    print(0)


solution()
