N, L, R = map(int, input().split())
nation = [list(map(int, input().split())) for _ in range(N)]
ans = 0


def bfs(r, c, nn, prev):
    for row, col in (r, c-1), (r, c+1), (r-1, c), (r+1, c):
        if 0 <= row < N and 0 <= col < N and (row, col) not in check and L <= abs(prev - nation[row][col]) <= R:
            check.add((row, col))
            nn.append((row, col))
            bfs(row, col, nn, nation[row][col])


while True:
    check = set()
    flag = False
    for r in range(N):
        for c in range(N):
            if (r, c) not in check:
                NN = []
                check.add((r, c))
                NN.append((r, c))
                bfs(r, c, NN, nation[r][c])

                if len(NN) > 1:
                    val = 0
                    for rr, cc in NN:
                        val += nation[rr][cc]

                    val //= len(NN)

                    flag |= len(NN)

                    for rr, cc in NN:
                        nation[rr][cc] = val
    if not flag:
        break
    ans += 1

print(ans)
