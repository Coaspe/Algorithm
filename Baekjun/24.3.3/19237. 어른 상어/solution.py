from sys import stdin

input = stdin.readline
N, M, K = map(int, input().split())
B = []
sharks = []

smell = [[(0, -1) for _ in range(N)] for _ in range(N)]
for i in range(N):
    t = []
    for j, v in enumerate(map(int, input().split())):
        tt = []
        if v:
            sharks.append([i, j])
            smell[i][j] = (0, v - 1)
            tt.append(v - 1)
        t.append(tt)
    B.append(t)

# 위 아래 왼쪽 오른쪽
SH = [v - 1 for v in map(int, input().split())]
D = [[[v - 1 for v in map(int, input().split())] for _ in range(4)] for _ in range(M)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = 0
while True:
    T += 1
    tmp_sharks = []

    for r, c in sharks:
        if not B[r][c]:
            continue

        shark = B[r][c][0]
        flag = False
        for next_direction in D[shark][SH[shark]]:
            row, col = r + dx[next_direction], c + dy[next_direction]

            if not (0 <= row < N and 0 <= col < N):
                continue

            if (
                smell[row][col][1] != -1
                and (T - smell[row][col][0] > K or smell[row][col][0] == T)
            ) or (smell[row][col][1] == -1):
                B[r][c].remove(shark)
                B[row][col].append(shark)
                tmp_sharks.append([row, col])
                SH[shark] = next_direction
                flag = True
                break

        if flag:
            continue

        for next_direction in D[shark][SH[shark]]:
            row, col = r + dx[next_direction], c + dy[next_direction]

            if not (0 <= row < N and 0 <= col < N):
                continue

            if smell[row][col][1] == shark:
                B[r][c].remove(shark)
                B[row][col].append(shark)
                tmp_sharks.append([row, col])
                SH[shark] = next_direction
                break
    L = 0
    for r in range(N):
        for c in range(N):
            B[r][c] = sorted(B[r][c])

            while len(B[r][c]) > 1:
                B[r][c].pop()

            if B[r][c]:
                smell[r][c] = (T, B[r][c][0])

            L += len(B[r][c])

    if L == 1 or T > 1000:
        break

    sharks = tmp_sharks

print(T if T <= 1000 else -1)
