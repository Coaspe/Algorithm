from collections import deque
MAX_NUM = 500000
N, K = map(int, input().split())
visited = [[-1 for _ in range(MAX_NUM + 1)] for _ in range(2)]


def bfs():
    q = deque()
    q.append((N, 0))
    visited[0][N] = 0

    while len(q):
        n, cnt = q.popleft()
        flag = cnt % 2

        for next_n in [n + 1, n - 1, 2 * n]:
            if 0 <= next_n <= MAX_NUM and visited[1-flag][next_n] == -1:
                visited[1-flag][next_n] = cnt+1
                q.append((next_n, cnt+1))


bfs()

t = 0
flag = 0
res = -1
while K <= 500000:
    if visited[flag][K] != -1:
        if visited[flag][K] <= t:
            res = t
            break
    flag = 1 - flag
    t += 1
    K += t

print(res)
