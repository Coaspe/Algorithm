from collections import deque
import math


def solultion():
    R, C = map(int, input().split())

    room = [list(input()) for _ in range(R)]
    check = [[[math.inf]*C for _ in range(R)] for _ in range(5)]

    def dToRC(x):
        if x == 0 or x == 2:
            return 0
        return 1
    '''
    # 어느 칸에서 어떤 방향으로 바리스타의 힘을 쓸 것인지 ...
    # (현재 노드, 소요 거리, 힘을 쓴 노드, 힘을 쓴 방향)
    # 힘을 쓴 방향
    -> -1: 아직 안 씀 0: 위, 1: 오른쪽, 2: 아래, 3: 왼쪽
    
    '''
    q = deque([((0, 0), 0, (-1, -1), -1)])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while q:
        node, dist, p_node, p_d = q.popleft()

        if node == (R-1, C-1):
            print(dist)
            return

        for i in range(4):
            row, col = node[0] + dx[i], node[1] + dy[i]
            if 0 <= row < R and 0 <= col < C and not check[p_d][row][col]:
                # 벽 일 때
                cc = (p_node[dToRC(p_d)] if p_d != -
                      1 else -1, p_d, (row, col))
                if room[row][col] == '1':
                    # 아직 힘을 안 썼을 때
                    if p_d == -1:
                        if not check[i][row][col]:
                            check[i][row][col] = 1
                            q.append(((row, col), dist+1, node, i))
                        check[p_d][row][col]
                    # 이미 힘을 쓴 상태
                    elif cc not in check:
                        sub_x, sub_y = row - p_node[0], col - p_node[1]
                        if ((sub_y < 0 and p_d == 3) or (sub_y > 0 and p_d == 1)) or \
                                ((sub_x < 0 and p_d == 0) or (sub_x > 0 and p_d == 2)):
                            check.add(cc)
                            q.append(((row, col), dist + 1, p_node, p_d))

                # 벽이 아닐 때
                elif cc not in check:
                    check.add(cc)
                    q.append(((row, col), dist+1, p_node, p_d))

    print(-1)


solultion()
