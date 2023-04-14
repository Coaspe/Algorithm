import heapq

N = int(input())
BSZ = 2
UP = 0
S = [list(map(int, input().split())) for _ in range(N)]
R = C = -1
time = 0

for r in range(N):
    for c in range(N):
        if S[r][c] == 9:
            R, C = r, c
            S[R][C] = 0
            break


def bfs(U, B):
    global R, C, time
    q = [(0, R, C)]
    check = [[0]*N for _ in range(N)]
    check[R][C] = 1

    while q:
        d, r, c = heapq.heappop(q)

        if S[r][c] and B > S[r][c]:
            S[r][c] = 0
            U += 1
            if U == B:
                U = 0
                B += 1
            R, C = r, c
            time += d
            return U, B

        for row, col in (r-1, c), (r, c-1), (r, c+1), (r+1, c):
            if 0 <= row < N and 0 <= col < N and not check[row][col] and B >= S[row][col]:
                check[row][col] = 1
                heapq.heappush(q, (d+1, row, col))

    return U, B


while 1:
    tup, tbsz = bfs(UP, BSZ)
    if tup == UP and tbsz == BSZ:
        break
    else:
        UP, BSZ = tup, tbsz

print(time)
