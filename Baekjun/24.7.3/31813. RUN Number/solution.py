import sys
from collections import deque

input = sys.stdin.readline
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
N, M, K = map(int, input().split())
p = [list(input()) for _ in range(N)]
check = [[0] * M for _ in range(N)]

bfs = deque()
for i in range(N * M):
    r = i // M
    c = i % M
    # 빈칸을 먼저 찾아서 bfs에 담는다.
    if p[r][c] == ".":
        bfs.append((r, c))

    # 너비우선탐색
    while bfs:
        nr, nc = bfs.popleft()
        nearby = 0  # 인접한 정상 체온의 수
        blanks = []  # 인접한 빈칸의 좌표를 담을 리스트
        for i in range(4):
            dr = nr + d[i][0]
            dc = nc + d[i][1]
            if 0 <= dr < N and 0 <= dc < M:
                if p[dr][dc] == ".":
                    blanks.append((dr, dc))
                else:
                    nearby += 1

            # 인접 정상 체온이 2이상인 경우
            if nearby >= 2:
                p[nr][nc] = "O"
                while blanks:
                    bfs.append(blanks.pop())

recovered = 0
bfs.clear()

# 직사각형 분포 탐색
for i in range(N * M):
    r = i // M
    c = i % M
    if p[r][c] == "O" and check[r][c] == 0:
        h, w = r, c
        # 직사각형의 가로와 세로 구하기
        while h < N and p[h][c] == "O":
            h += 1
        while w < M and p[r][w] == "O":
            w += 1
        for j in range(r, h):
            for k in range(c, w):
                check[j][k] = 1

        # K보다 작은 변을 갖는 직사각형은 버림
        if h - r > K and w - c > K:
            recovered += (h - r) * (w - c)
print(recovered)
