from collections import defaultdict, deque
N, M = map(int, input().split())
# 0 - Not available, 1 - availabe, 2 - visited
check = [[0]*(N+1) for _ in range(N+1)]
check[1][1] = 2
sw = defaultdict(list)
counted = set([(1, 1)])

# (x, y)
q = deque([(1, 1)])

for _ in range(M):
    x, y, a, b = map(int, input().split())
    sw[(x, y)].append((a, b))

while q:
    x, y = q.popleft()

    for swx, swy in sw[(x, y)]:
        if check[swx][swy] == 0:
            check[swx][swy] = 1
            counted.add((swx, swy))
            for nx, ny in (swx+1, swy), (swx-1, swy), (swx, swy-1), (swx, swy+1):
                if 1 <= nx <= N and 1 <= ny <= N and check[nx][ny] == 2:
                    check[swx][swy] = 2
                    q.append((swx, swy))
                    break

    sw[(x, y)] = []

    for nx, ny in (x+1, y), (x-1, y), (x, y-1), (x, y+1):
        if 1 <= nx <= N and 1 <= ny <= N and check[nx][ny] == 1:
            q.append((nx, ny))
            check[nx][ny] = 2

print(len(counted))
