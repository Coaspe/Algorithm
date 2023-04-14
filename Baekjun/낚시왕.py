import sys

input = sys.stdin.readline

DELTA = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]

R, C, M = map(int, input().split())

matrix = [[None] * C for _ in range(R)]

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    matrix[r - 1][c - 1] = (s, d, z)

answer = 0
for j in range(C):
    # 낚시
    for i in range(R):
        if matrix[i][j]:
            answer += matrix[i][j][2]
            matrix[i][j] = None
            break

    # 상어 이동
    new_matrix = [[None] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if not matrix[r][c]:
                continue
            s, d, z = matrix[r][c]

            if d > 2:
                nr = r
                nc = c + s * DELTA[d][1]
                qc, rc = divmod(nc, C - 1)
                if qc % 2 == 0:
                    nc = rc
                else:
                    d = ((d - 2) % 2) + 3
                    nc = (C - 1) - rc
            else:
                nc = c
                nr = r + s * DELTA[d][0]
                qr, rr = divmod(nr, R - 1)
                if qr % 2 == 0:
                    nr = rr
                else:
                    d = (d % 2) + 1
                    nr = (R - 1) - rr

            if not new_matrix[nr][nc] or new_matrix[nr][nc][2] < z:
                new_matrix[nr][nc] = (s, d, z)

    matrix = new_matrix

print(answer)
