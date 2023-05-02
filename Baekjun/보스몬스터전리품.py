from collections import defaultdict, deque

M, N, P = map(int, input().split())
MAP = [input() for _ in range(M)]

ploc = defaultdict(int)
boss = (-1, -1)
for m in range(M):
    for n in range(N):
        if MAP[m][n] == 'B':
            boss = (m, n)
        elif MAP[m][n] == '.' or MAP[m][n] == 'X':
            continue
        else:
            ploc[MAP[m][n]] = (m, n)

dps = defaultdict(int)

for _ in range(len(ploc)):
    p, d = input().split()
    dps[p] = int(d)

hp = int(input())

q = deque([(*boss, 0)])
ch = [[False]*N for _ in range(M)]
ch[boss[0]][boss[1]] = True

dist = defaultdict(int)
while P and q:
    r, c, d = q.popleft()

    for row, col in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
        if 0 <= row < M and 0 <= col < N and not ch[row][col] and MAP[row][col] != 'X':
            ch[row][col] = True
            if MAP[row][col] != '.':
                P -= 1
                dist[MAP[row][col]] = d+1
            q.append((row, col, d+1))
arrived = []
ans = set()
while hp > 0:
    for key in dist.keys():
        dist[key] -= 1
        if dist[key] == 0:
            arrived.append(key)

    for user in arrived:
        hp -= dps[user]
        ans.add(user)

print(len(ans))
