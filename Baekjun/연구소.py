from itertools import combinations
from collections import deque
N, M = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(N)]

zeros = []

for i in range(N):
    for j in range(M):
        if mat[i][j] == 0:
            zeros.append((i, j))

permu = combinations(zeros, 3)


def process(x, y, visited):
    q = deque([(x, y)])

    while q:
        r, c = q.popleft()

        for row, col in (r, c+1), (r, c-1), (r+1, c), (r-1, c):
            if 0 <= row < N and 0 <= col < M and (row, col) not in visited and mat[row][col] == 0:
                visited.add((row, col))
                q.append((row, col))


answer = 0
for p in permu:
    p1, p2, p3 = p
    mat[p1[0]][p1[1]] = 1
    mat[p2[0]][p2[1]] = 1
    mat[p3[0]][p3[1]] = 1
    visited = set()
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 2:
                process(i, j, visited)
    answer = max(answer, len(zeros) - len(visited) - 3)
    mat[p1[0]][p1[1]] = 0
    mat[p2[0]][p2[1]] = 0
    mat[p3[0]][p3[1]] = 0
print(answer)
