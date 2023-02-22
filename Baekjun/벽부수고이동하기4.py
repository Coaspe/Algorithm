from collections import deque
R, C = map(int, input().split())
room = [list(map(int, input())) for _ in range(R)]
room2 = [[0]*C for _ in range(R)]
visited = [[False]*C for _ in range(R)]
parent = [[(r, c) for c in range(C)] for r in range(R)]
setset = [[1]*C for _ in range(R)]
rank = [[0]*C for _ in range(R)]


def find(r, c):
    if parent[r][c] != (r, c):
        parent[r][c] = find(*parent[r][c])
    return parent[r][c]


def union(v1, v2):
    if v1 == (None, None) or v2 == (None, None):
        return
    p1 = find(v1[0], v1[1])
    p2 = find(v2[0], v2[1])

    parent[p2[0]][p2[1]] = p1
    setset[p1[0]][p1[1]] += 1


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(r, c):
    q = deque([(r, c)])
    visited[r][c] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and room[nx][ny] == 0:
                union((x, y), (nx, ny))
                visited[nx][ny] = True
                q.append((nx, ny))


for r in range(R):
    for c in range(C):
        if room[r][c] == 0 and not visited[r][c]:
            visited[r][c] = True
            bfs(r, c)

for r in range(R):
    for c in range(C):
        if room[r][c] == 1:
            check = set()
            ans = 1
            for i in range(4):
                nx, ny = r+dx[i], c+dy[i]
                if 0 <= nx < R and 0 <= ny < C and room[nx][ny] == 0:
                    nx, ny = find(nx, ny)
                    if not (nx, ny) in check:
                        check.add((nx, ny))
                        ans += setset[nx][ny]
            room2[r][c] = ans % 10
for i in room2:
    print("".join(map(str, i)))
