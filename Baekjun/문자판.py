import collections
N, M, K = map(int, input().split())
B = [input() for _ in range(N)]
WORD = input()
start = []
for r in range(N):
    for c in range(M):
        if B[r][c] == WORD[0]:
            start.append((r, c))
dx = [0]*2*K + [i for i in range(-K, 0)] + [i for i in range(1, K+1)]
dy = dx[::-1]
ans = 0
check = [[[-1] * len(WORD) for _ in range(M)] for _ in range(N)]


def dfs(r, c, idx):
    if idx == len(WORD):
        return 1
    if check[r][c][idx] != -1:
        return check[r][c][idx]

    check[r][c][idx] = 0

    for i in range(len(dx)):
        nx, ny = r+dx[i], c+dy[i]
        if 0 <= nx < N and 0 <= ny < M and B[nx][ny] == WORD[idx]:
            check[r][c][idx] += dfs(nx, ny, idx+1)
    return check[r][c][idx]


for r, c in start:
    ans += dfs(r, c, 1)
print(ans)
