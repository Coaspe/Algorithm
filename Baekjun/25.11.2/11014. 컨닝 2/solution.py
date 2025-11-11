dx, dy = [-1, 0, 1, 1, 0, -1], [-1, -1, -1, 1, 1, 1]


for _ in range(int(input())):
    N, M = map(int, input().split())

    def f(x, y):
        return x * M + y

    B = [list(input()) for _ in range(N)]

    T = 0
    for i in range(N):
        for j in range(M):
            T += int(B[i][j] == ".")

    G = [[] for _ in range(N * M)]

    for i in range(N):
        for j in range(M):
            if B[i][j] != ".":
                continue
            for k in range(6):
                ii = i + dx[k]
                jj = j + dy[k]

                if 0 <= ii < N and 0 <= jj < M and B[ii][jj] == ".":
                    G[f(i, j)].append(f(ii, jj))

    p = [-1] * N * M

    def dfs(chk, v):
        for next_v in G[v]:
            if chk[next_v]:
                continue

            chk[next_v] = 1

            if p[next_v] == -1 or dfs(chk, p[next_v]):
                p[next_v] = v
                return 1
        return 0

    for i in range(N):
        for j in range(0, M, 2):
            if B[i][j] != ".":
                continue

            chk = [0] * N * M

            v = f(i, j)
            chk[v] = 1

            T -= dfs(chk, v)

    print(T)
