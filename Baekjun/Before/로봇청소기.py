import sys
from collections import deque


def find_start(vv, my_map, n, m):
    for i in range(n):
        for j in range(m):
            if my_map[i][j] == 'o':
                start = (i, j)
            elif my_map[i][j] == '*':
                vv.append((i, j))

    return start

# BFS 함수


def bfs(n, m, my_map):

    # 변수 초기화
    que = deque()
    answer = 9876543210
    vv = []
    start = find_start(vv, my_map, n, m)

    # 방문 배열 초기화
    # 2**(len(vv)) + 1 경우의 수만큼 3차원 배열을 만듦 (비트마스킹)
    v = [[[9876543210 for _ in range(m)] for _ in range(n)]
         for _ in range(2**(len(vv)) + 1)]

    # 전체 쓰레기 갯수, 종료 조건
    d_cnt = len(vv)
    que.append((start[0], start[1], 0, 0, 0))

    while que:
        r, c, cnt, time, status = que.popleft()

        if cnt == d_cnt:
            answer = min(answer, time)
            break

        for row, col in (r + 1, c), (r-1, c), (r, c+1), (r, c-1):
            if 0 <= row < n and 0 <= col < m:
                if my_map[row][col] == '.' or my_map[row][col] == 'o':
                    if v[status][row][col] > time + 1:
                        v[status][row][col] = time+1
                        que.append((row, col, cnt, time+1, status))
                elif my_map[row][col] == '*':
                    if status & 1 << vv.index((row, col)) == 0:
                        newStatus = status | 1 << vv.index((row, col))
                        v[newStatus][row][col] = time+1
                        que.append((row, col, cnt + 1, time + 1, newStatus))
                    else:
                        if v[status][row][col] > time + 1:
                            v[status][row][col] = time + 1
                            que.append((row, col, cnt, time+1, status))

            # answer가 초기값 그대로면 -1
    if answer == 9876543210:
        print(-1)
        return
    else:
        print(answer)
        return


while 1:

    # 변수 입력 받기
    m, n = map(int, sys.stdin.readline().split())
    if m == 0 and n == 0:
        break
    else:
        my_map = []
        for _ in range(n):
            my_map.append(str(sys.stdin.readline().rstrip()))

        bfs(n, m, my_map)
