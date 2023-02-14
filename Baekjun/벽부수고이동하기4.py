from collections import deque
R, C = map(int, input().split())
room = [input() for _ in range(R)]
parent = [[(-1, -1)]*C for _ in range(R)]
setset = [[0]*C for _ in range(R)]
q = deque([])


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


def dfs(prev, curr):
    union(prev, curr)
    for i in range(4):
        nx, ny = curr[0]+dx[i], curr[1]+dy[i]
        if 0 <= nx < R and 0 <= ny < C and room[nx][ny] == '0':
            if (nx, ny) not in visited:
                visited.add(curr)
                dfs(curr, (nx, ny))


visited = set()
for r in range(R):
    for c in range(C):
        if room[r][c] == '0':
            setset[r][c] += 1
            visited.add((r, c))
            parent[r][c] = (r, c)
            dfs((None, None), (r, c))

print(setset)
print(find(0, 2), find(0, 3))
