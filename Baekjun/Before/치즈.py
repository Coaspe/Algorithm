from collections import deque
N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
ch = set()
ans = 0
for n in range(N):
    for m in range(M):
        if paper[n][m] == 1:
            ch.add((n, m))


def bfs(rr, cc, check):
    wall = False
    q = deque([(rr, cc)])
    stack = []
    while q:
        r, c = q.popleft()
        stack.append((r, c))

        if r == N - 1 or c == M - 1:
            wall = True

        for row, col in (r, c-1), (r, c+1), (r+1, c), (r-1, c):
            if 0 <= row < N and 0 <= col < M and paper[row][col] != 1 and not check[row][col]:
                check[row][col] = 1
                q.append((row, col))

    for r, c in stack:
        paper[r][c] = 0 if wall else 2


while ch:
    ans += 1
    check = [[0]*M for _ in range(N)]
    soon = set()

    for r, c in ch:
        air = 0
        for row, col in (r, c-1), (r, c+1), (r+1, c), (r-1, c):
            if 0 <= row < N and 0 <= col < M and paper[row][col] != 1:
                if not check[row][col]:
                    bfs(row, col, check)
                air += int(paper[row][col] == 0)
        if air >= 2:
            soon.add((r, c))

    for r, c in soon:
        paper[r][c] = 0
        ch.remove((r, c))

print(ans)
