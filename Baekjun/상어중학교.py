from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 무지개 : 0, 검정 블록: -1
# 일반블록: 나머지


def bfs(r1, c2, check):
    q = deque([(r1, c2)])
    color = board[r1][c2]
    retval = set([(r1, c2)])
    rainbow = 0
    standard = (r1, c2)
    while q:
        r, c = q.popleft()

        for row, col in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
            if 0 <= row < N and 0 <= col < N and (not board[row][col] or board[row][col] == color) and (row, col) not in retval:
                retval.add((row, col))
                q.append((row, col))
                if board[row][col]:
                    check.add((row, col))
                    standard = min(standard, (row, col),
                                   key=lambda x: (x[0], x[1]))
                else:
                    rainbow += 1

    return retval, rainbow, standard


def gravity(board):
    for r in range(N-1, -1, -1):
        for c in range(N):
            if board[r][c] >= 0:
                x = r
                while x + 1 < N and board[x+1][c] == -2:
                    x += 1
                if x != r:
                    board[r][c], board[x][c] = board[x][c], board[r][c]


ans = 0
while True:
    # 가장 큰 그룹 찾기
    check = set()
    largest, l_rainbow, l_standard = [], 0, (0, 0)
    for r in range(N):
        for c in range(N):
            if (r, c) not in check and board[r][c] > 0:
                B, rainbow, standard = bfs(r, c, check)

                if len(B) < 2:
                    continue

                # 더 많은 블록이 있는 그룹
                if len(largest) == len(B):
                    # 무지개가 더 많은 그룹
                    if l_rainbow == rainbow:
                        # 기준 블록의 행, 열이 더 큰 그룹
                        if l_standard[0] == standard[0]:
                            largest = largest if l_standard[1] > standard[1] else B
                        else:
                            largest = largest if l_standard[0] > standard[0] else B

                    else:
                        largest = largest if l_rainbow > rainbow else B
                else:
                    largest = max(largest, B, key=lambda x: len(x))

                if largest == B:
                    l_rainbow, l_standard = rainbow, standard
    if not len(largest):
        break
    ans += len(largest) * len(largest)

    for r, c in largest:
        board[r][c] = -2

    # 중력 작용
    gravity(board)

    # 회전
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[N - j - 1][i] = board[i][j]

    board = result

    # 중력 작용
    gravity(board)

print(ans)
