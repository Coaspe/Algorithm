import collections
R, C = map(int, input().split())

cave = [list(input().strip()) for _ in range(R)]
qn = int(input())
Q = list(map(int, input().split()))


def findBottom(row, col, chunck):
    for r in range(row + 1, R):
        if cave[r][col] == 'x' and (r, col) not in chunck:
            return r-1
    return R-1


def bfs(r, c):
    queue = collections.deque([(r, c)])
    chunck = set([(r, c)])
    while queue:
        r, c = queue.popleft()
        if r == R-1:
            chunck, minDist = False, False
        for row, col in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
            if 0 <= row <= R-1 and 0 <= col <= C-1 and cave[row][col] == 'x' and (row, col) not in visited:
                visited.add((row, col))
                if chunck:
                    chunck.add((row, col))
                queue.append((row, col))
    if chunck:
        minDist = 1000

        for row, col in chunck:
            minDist = min(minDist, abs(findBottom(row, col, chunck)-row))

    return chunck, minDist


for i in range(qn):
    q = Q[i]
    visited = set()
    left = i % 2 == 0
    ran = range(C) if left else range(C-1, -1, -1)
    for j in ran:
        if cave[R-q][j] == 'x':
            cave[R-q][j] = '.'
            for r, c in (R-q-1, j), (R-q, j + (1 if left else -1)), (R-q+1, j):
                if 0 <= r < R and 0 <= c < C and cave[r][c] == 'x' and (r, c) not in visited:
                    visited.add((r, c))
                    chunck, minDist = bfs(r, c)
                    if chunck:
                        for r, c in sorted(chunck, key=lambda x: -x[0]):
                            cave[r][c] = '.'
                            cave[r+minDist][c] = 'x'
                        break
            break
for i in range(R):
    for j in range(C):
        print(cave[i][j], end="")
    print()
