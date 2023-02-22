from collections import deque
import math
N, M, K = map(int, input().split())
room = [list(map(int, input())) for _ in range(N)]
visited = [[K+1] * M for _ in range(N)]
visited[0][0] = 0
q = deque([(1, 0, 0)])
ans = math.inf
while q:
    move, r, c = q.popleft()
    if (r, c) == (N-1, M-1):
        ans = move
        break

    for row, col in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
        if 0 <= row < N and 0 <= col < M:
            temp = room[row][col] + visited[r][c]
            if temp < visited[row][col] and temp <= K:
                q.append((move+1, row, col))
                visited[row][col] = temp

print(ans if ans != math.inf else -1)
