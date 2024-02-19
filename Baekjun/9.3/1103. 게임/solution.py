N, M = map(int, input().split())


def tr(x):
    if x == "H":
        return x
    return int(x)


B = [list(map(tr, list(input()))) for _ in range(N)]
C = [[0] * M for _ in range(N)]
check = [[0] * M for _ in range(N)]


def dfs(r, c, cnt):
    check[r][c] = cnt

    d = B[r][c]

    if d == "H":
        return cnt - 1

    cc = cnt
    for row, col in (r + d, c), (r - d, c), (r, c + d), (r, c - d):
        if 0 <= row < N and 0 <= col < M:
            if C[row][col]:
                print(-1)
                exit(0)

            if cnt + 1 > check[row][col]:
                C[row][col] = 1
                k = dfs(row, col, cnt + 1)

                if k == -1:
                    return k

                cc = max(cc, k)
                C[row][col] = 0

    return cc


print(dfs(0, 0, 1))
