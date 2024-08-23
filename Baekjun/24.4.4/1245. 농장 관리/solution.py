from sys import stdin
from collections import deque


def solution():
    input = stdin.readline
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    C = [[0] * M for _ in range(N)]
    dx, dy = [0, 0, 1, 1, 1, -1, -1, -1], [1, -1, 0, -1, 1, 0, -1, 1]
    ans = 0

    for h in range(1, 501):
        for x in range(N):
            for y in range(M):
                if B[x][y] != h or C[x][y]:
                    continue

                flag = True
                q = deque([(x, y)])

                C[x][y] = 1
                while q:
                    r, c = q.popleft()

                    for i in range(8):
                        row, col = r + dx[i], c + dy[i]

                        if 0 <= row < N and 0 <= col < M and not C[row][col]:
                            if B[row][col] == B[r][c]:
                                q.append((row, col))
                                C[row][col] = 1
                            elif B[row][col] > B[r][c]:
                                flag = False

                ans += int(flag)

    print(ans)


if __name__ == "__main__":
    solution()
