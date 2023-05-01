from collections import deque
N, Q = map(int, input().split())
R = C = pow(2, N)
board = [list(map(int, input().split())) for _ in range(R)]
op = list(map(int, input().split()))

for o in op:
    step = pow(2, o)
    new_board = [[] for _ in range(R)]
    if o != 0:
        for r in range(0, R, step):
            for c in range(0, R, step):
                new_arr = []
                for r1 in range(r, r+step):
                    new_arr.append(board[r1][c:c+step])

                new_arr = list(zip(*new_arr[::-1]))

                for r1 in range(r+step-1, r-1, -1):
                    for e in new_arr.pop():
                        new_board[r1].append(e)
    else:
        new_board = board
    tmp_board = [x[:] for x in new_board]

    # Check zeros
    for r in range(R):
        for c in range(C):

            if not new_board[r][c]:
                continue

            check = 0

            for row, col in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                if 0 <= row < R and 0 <= col < C and new_board[row][col]:
                    check += 1

            if check <= 2:
                tmp_board[r][c] -= 1

    board = tmp_board

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)


def check_ice_bfs(board, len_board):
    """
    얼음 상태 확인
    :param board: 보드
    :param len_board: 보드 가로 길이
    :return:
    """
    used = [[False] * len_board for _ in range(len_board)]
    ice_sum = 0
    max_area_count = 0
    for y in range(len_board):
        for x in range(len_board):
            area_count = 0
            if used[y][x] or board[y][x] == 0:
                continue
            # BFS를 이용하여 얼음 덩어리 조사
            q = deque()
            q.append((y, x))
            used[y][x] = True

            while q:
                sy, sx = q.popleft()
                ice_sum += board[sy][sx]  # 얼음 합 추가
                area_count += 1  # 얼음 카운트 추가

                for d in range(4):
                    ny = sy + dy[d]
                    nx = sx + dx[d]
                    if nx < 0 or ny < 0 or nx >= len_board or ny >= len_board or used[ny][nx]:
                        continue
                    if board[ny][nx] != 0:
                        used[ny][nx] = True
                        q.append((ny, nx))

            max_area_count = max(max_area_count, area_count)  # 최대 얼음 덩어리 크기 파악

    print(ice_sum)
    print(max_area_count)


check_ice_bfs(board, R)
