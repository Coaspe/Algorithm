from sys import stdin
from itertools import permutations
from collections import deque

input = stdin.readline
N, M = map(int, input().split())
B = [list(input()) for _ in range(N)]

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

for i in range(N):
    for j in range(M):
        if B[i][j] == "S":
            start = (i, j)


def find(start):
    visited = [[0] * M for _ in range(N)]
    dq = deque([(start[0], start[1], 0)])
    visited[start[0]][start[1]] = 1

    dist = {}

    while dq:
        r, c, t = dq.popleft()

        for i in range(4):
            rr, cc = r + dx[i], c + dy[i]

            if (
                0 <= rr < N
                and 0 <= cc < M
                and visited[rr][cc] == 0
                and B[rr][cc] != "X"
            ):
                visited[rr][cc] = 1
                dq.append((rr, cc, t + 1))

                if B[rr][cc] == "K":
                    dist[(rr, cc)] = t + 1

    return dist


fromStart = find(start)
if len(fromStart) < 5:
    print(-1)
    exit(0)


candid = list(fromStart.keys())


ans = float("inf")

dist = [fromStart]
for c in candid:
    dist.append(find(c))

for p in permutations(range(len(fromStart)), 5):
    tmp_ans = 0
    prev = 0
    for i, v in enumerate(p):
        tmp_ans += dist[prev][candid[v]]
        prev = v + 1

    ans = min(ans, tmp_ans)

print(ans)
