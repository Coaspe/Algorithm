from sys import stdin
from collections import deque
input = stdin.readline

dy = (-1, 0, 1, 0)
dx = (0, -1, 0, 1)

# 큐에서 백조가 될 수도 있는 후보군을 탐색


def find_swan(lake, visited, queue):
    next_queue = deque()
    while queue:
        y, x = queue.popleft()
        if y == swan[1][0] and x == swan[1][1]:
            return True, None

        for ii in range(4):
            ny = y + dy[ii]
            nx = x + dx[ii]
            if 0 <= ny < row and 0 <= nx < column and not visited[ny][nx]:
                # 다음 melt ice에서 녹는 얼음
                if lake[ny][nx] == 'X':
                    next_queue.append((ny, nx))
                # L or .
                else:
                    queue.append((ny, nx))
                visited[ny][nx] = True

    return False, next_queue

# 얼음을 물로 바꾸고
# 이번에 물이 된 좌표를 반환


def melt_ice(water, lake):
    next_water = deque()
    while water:
        y, x = water.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not 0 <= ny < row or not 0 <= nx < column:
                continue
            if lake[ny][nx] == 'X':
                next_water.append((ny, nx))
                lake[ny][nx] = '.'

    return next_water


row, column = map(int, input().split())
lake = []
swan = []
water = deque()

for rr in range(row):
    current_lake_info = list(input().rstrip())
    for cc, vv in enumerate(current_lake_info):
        if vv == '.' or vv == 'L':
            water.append((rr, cc))
        if vv == 'L':
            swan.append((rr, cc))
    lake.append(current_lake_info)

day = -1
visited = [[False for _ in range(column)] for _ in range(row)]
queue = deque()

y, x = swan[0][0], swan[0][1]
queue.append((y, x))
visited[y][x] = True

while True:
    day += 1
    found, next_queue = find_swan(lake, visited, queue)
    queue = next_queue
    if found:
        break
    water = melt_ice(water, lake)

print(day)
