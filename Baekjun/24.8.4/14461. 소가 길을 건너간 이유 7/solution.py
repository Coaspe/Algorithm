from heapq import *
from sys import maxsize

N, T = map(int, input().split())

B = [list(map(int, input().split())) for _ in range(N)]

inf = maxsize
C = [[[inf] * 4 for _ in range(N)] for _ in range(N)]
C[0][0][0] = 0

# time, r, c, cnt
q = [(0, 0, 0, 0)]
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

while q:
    t, r, c, cnt = heappop(q)

    if t > C[r][c][cnt]:
        continue

    for i in range(4):
        rr, cc = r + dx[i], c + dy[i]
        new_t = t + T
        if 0 <= rr < N and 0 <= cc < N:
            if cnt == 3:
                new_t += B[r][c]

            if cnt == 2 and (rr, cc) == (N - 1, N - 1):
                new_t += B[rr][cc]

            new_cnt = 1 if cnt == 3 else (cnt + 1)
            if C[rr][cc][new_cnt] > new_t:
                C[rr][cc][new_cnt] = new_t
                heappush(q, (new_t, rr, cc, new_cnt))

print(min(C[-1][-1]))
