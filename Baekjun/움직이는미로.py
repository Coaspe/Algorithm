from collections import deque
R = C = 8
maze = [input() for _ in range(8)]


def solve():
    # row, col, count
    q = deque([(7, 0, 0)])
    visited = set()

    while q:
        r, c, count = q.popleft()
        if (r, c) in visited:
            visited.remove((r, c))
        if r == 0 and c == 7:
            print(1)
            return

        for row, col in (r-1, c+1), (r, c+1), (r-1, c), (r+1, c+1), (r, c), (r, c-1), (r+1, c), (r-1, c-1), (r+1, c-1):
            if (row, col) not in visited and 0 <= row < R and 0 <= col < C \
                    and (row-count < 0 or maze[row-count][col] != '#') \
                    and (row-count-1 < 0 or maze[row-count-1][col] != '#'):
                visited.add((row, col))
                if row > r or col < c:
                    q.appendleft((row, col, count+1))
                else:
                    q.append((row, col, count+1))
    print(0)


solve()
