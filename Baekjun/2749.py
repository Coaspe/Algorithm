import math
import collections
T = int(input())
WALL, SPACE, DOOR, PRISONER = '*', '.', '#', '$'


def entrance_to_p1(rr, cc, p1):
    visited = set([(rr, cc)])
    q = collections.deque(
        [(int(prison[rr][cc] == DOOR), rr, cc, set([(rr, cc)]))])
    minpath = (math.inf, None)
    while q:
        n, r, c, path = q.popleft()
        if n > minpath[0]:
            continue
        if (r, c) == p1:
            minpath = min(minpath, (n, path), key=lambda x: x[0])
            continue
        for row, col in (r+1, c), (r-1, c), (r, c-1), (r, c+1):
            if 0 <= row <= rows-1 and 0 <= col <= cols-1 and prison[row][col] != WALL and (row, col) not in visited:
                visited.add((row, col))
                path = set(path)
                path.add((row, col))
                q.append((int(prison[row][col] == DOOR) + n, row, col, path))

    return minpath


def p2_to_entrance(rr, cc, path):
    visited = set([(rr, cc)])
    q = collections.deque([(0, rr, cc)])
    minpath = math.inf
    while q:
        n, r, c = q.popleft()
        if n > minpath:
            continue
        if r == 0 or r == rows-1 or c == 0 or c == cols - 1:
            minpath = min(minpath, n)
            continue
        for row, col in (r+1, c), (r-1, c), (r, c-1), (r, c+1):
            if 0 <= row <= rows-1 and 0 <= col <= cols-1 and prison[row][col] != WALL and (row, col) not in visited:
                visited.add((row, col))
                q.append((int(prison[row][col] == DOOR and (
                    row, col) not in path) + n, row, col))
    return minpath


while T:
    T -= 1

    rows, cols = map(int, input().split())
    prison = [list(input().strip()) for _ in range(rows)]
    entrance = set()
    prisoner = []
    for i in range(rows):
        for j in range(cols):
            if prison[i][j] != WALL:
                if i == 0 or i == rows-1:
                    entrance.add((i, j))
                else:
                    if j == 0 or j == cols-1:
                        entrance.add((i, j))
            if prison[i][j] == PRISONER:
                prisoner.append((i, j))

    p1, p2 = prisoner[0], prisoner[1]
    ans = math.inf
    for r, c in entrance:
        n, path = entrance_to_p1(r, c, p1)
        if path:
            n += p2_to_entrance(p2[0], p2[1], path)
            ans = min(ans, n)

    print(ans)
