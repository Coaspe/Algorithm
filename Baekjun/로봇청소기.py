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
        r, c, cnt, time, dirty_status = que.popleft()
        if cnt == d_cnt:
            answer = min(time, answer)

        for rr, cc in tra_list:
            next_r = r + rr
            next_c = c + cc
            if -1 < next_r < n and -1 < next_c < m:

                # 일반 통로나 로봇 청소기 시작 지점을 만남
                # 현재 쓰레기 상태에서 이전에 방문했는지 확인 후, 방문하지 않으면 추가 탐색한다.
                if my_map[next_r][next_c] == '.' or my_map[next_r][next_c] == 'o':
                    if v[dirty_status][next_r][next_c] > time + 1:
                        v[dirty_status][next_r][next_c] = time + 1
                        que.append(
                            (next_r, next_c, cnt, time + 1, dirty_status))

                # 쓰레기를 만남.
                # 처음 만난 쓰레기라면, 쓰레기 상태를 업데이트 해준 후, 업데이트 한 쓰레기 상태의 방문 노드에 방문 처리 해준다.
                elif my_map[next_r][next_c] == '*':
                    if dirty_status & 1 << vv.index((next_r, next_c)) == 0:
                        next_dirty_status = dirty_status | 2 ** vv.index(
                            (next_r, next_c))
                        v[next_dirty_status][next_r][next_c] = time + 1
                        que.append((next_r, next_c, cnt + 1,
                                   time + 1, next_dirty_status))

                # 내가 이미 치웠던 쓰레기라면, 현재 쓰레기 상태로 여기를 온 적이 있는지 확인.
                # 일전에 이 상태로 온 적디 없다면, 현재 쓰레기 상태에서 방문 처리 한 후 추가 탐색한다.

                    else:
                        if v[dirty_status][next_r][next_c] > time + 1:
                            v[dirty_status][next_r][next_c] = time + 1
                            que.append(
                                (next_r, next_c, cnt, time + 1, dirty_status))

    # answer가 초기값 그대로면 -1
    if answer == 9876543210:
        print(-1)
        return
    else:
        print(answer)
        return


tra_list = [[1, 0], [0, 1], [-1, 0], [0, -1]]
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
