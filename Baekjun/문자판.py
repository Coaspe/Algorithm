N, M, K = map(int, input().split())
G = [input() for _ in range(N)]
WORD = input()

D = [[[-1 for _ in range(len(WORD))] for _ in range(M)] for _ in range(N)]

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]


def DFS(x, y, idx):

    if idx == 0:
        D[x][y][0] = 1
        return 1

    tmp = 0
    for k in range(1, K+1):
        for d in range(4):
            nx, ny = x+dx[d]*k, y+dy[d]*k
            if 0 <= nx < N and 0 <= ny < M:
                if G[nx][ny] == WORD[idx-1]:
                    if D[nx][ny][idx-1] == -1:
                        DFS(nx, ny, idx-1)
                    tmp += D[nx][ny][idx-1]
    D[x][y][idx] = tmp
    return D[x][y][idx]


answer = 0
for x in range(N):
    for y in range(M):
        if G[x][y] == WORD[-1]:
            if D[x][y][len(WORD)-1] == -1:
                answer += DFS(x, y, len(WORD)-1)
            else:
                answer += D[x][y][len(WORD)-1]

print(answer)
