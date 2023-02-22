from collections import deque

n, m, k = map(int, input().split())
board = [input().strip() for _ in range(n)]
visited = [[k + 1 for _ in range(m)] for _ in range(n)]
visited[0][0] = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

dq = deque()
dq.append([0, 0, 0])
cnt = 1
day = True

while dq:
    for _ in range(len(dq)):
        y, x, w = dq.popleft()

        if y == n - 1 and x == m - 1:
            print(cnt)
            exit(0)

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] > w:
                # 벽이 아닌 경우 낮이든 밤이든 이동 가능
                if board[ny][nx] == '0':
                    dq.append([ny, nx, w])
                    visited[ny][nx] = w
                # 벽인 경우
                elif w < k:
                    if not day:  # 밤 인 경우
                        dq.append([y, x, w])
                    else:
                        visited[ny][nx] = w
                        dq.append([ny, nx, w + 1])
    cnt += 1
    day = not day
print(-1)
