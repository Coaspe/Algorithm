from collections import deque


def solve():
    n, m = map(int, input().split())
    grid = [input() for _ in range(m)]

    start = None
    end = None
    items = []

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "S":
                start = (i, j)
            elif grid[i][j] == "E":
                end = (i, j)
            elif grid[i][j] == "X":
                items.append((i, j))

    num_items = len(items)

    queue = deque([(start[0], start[1], 0, 0)])
    visited = set([(start[0], start[1], 0)])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        row, col, collected, steps = queue.popleft()

        if collected == (1 << num_items) - 1 and grid[row][col] == "E":
            return steps

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] != "#":
                new_collected = collected

                if grid[new_row][new_col] == "X":
                    item_index = items.index((new_row, new_col))
                    new_collected |= 1 << item_index

                if (new_row, new_col, new_collected) not in visited:
                    visited.add((new_row, new_col, new_collected))
                    queue.append((new_row, new_col, new_collected, steps + 1))

    return -1


print(solve())
