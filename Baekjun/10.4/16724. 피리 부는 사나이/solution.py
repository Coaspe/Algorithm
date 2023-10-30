from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
B = [list(input()) for _ in range(N)]

F = {
    "D": lambda r, c: (r + 1, c),
    "U": lambda r, c: (r - 1, c),
    "R": lambda r, c: (r, c + 1),
    "L": lambda r, c: (r, c - 1),
}

parent = [[i * M + j for j in range(M)] for i in range(N)]


def find(r, c):
    if parent[r][c] != r * M + c:
        parent[r][c] = find(parent[r][c] // M, parent[r][c] % M)
    return parent[r][c]


def union(r1, c1, r2, c2):
    p1 = find(r1, c1)
    p2 = find(r2, c2)

    flag = p1 != p2

    if flag:
        parent[p1 // M][p1 % M] = p2

    return flag


ans = 0


for r1 in range(N):
    for c2 in range(M):
        r, c = r1, c2
        while True:
            if B[r][c] == "#":
                break

            nr, nc = F[B[r][c]](r, c)
            B[r][c] = "#"

            if not union(r, c, nr, nc):
                break

            r, c = nr, nc

        if parent[r1][c2] == r1 * M + c2:
            ans += 1

print(ans)
