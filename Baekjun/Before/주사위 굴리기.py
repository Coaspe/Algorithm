N, M, x, y, K = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(N)]

op = list(map(int, input().split()))
opMap = {
    1: "EAST",
    2: "WEST",
    3: "NORTH",
    4: "SOUTH",
}


def process(tmp):
    if mat[x][y] == 0:
        mat[x][y] = tmp
        D[2] = tmp
    else:
        D[2] = mat[x][y]
        mat[x][y] = 0
    print(D[5])


D = [0] * 6
for o in op:
    if opMap[o] == "EAST":
        if 0 <= y + 1 < M:
            y += 1
            tmp = D[3]
            D[3], D[1], D[5] = D[5], D[2], D[1]
            process(tmp)
    elif opMap[o] == "WEST":
        if 0 <= y - 1 < M:
            y -= 1
            tmp = D[1]
            D[3], D[1], D[5] = D[2], D[5], D[3]
            process(tmp)
    elif opMap[o] == "NORTH":
        if 0 <= x - 1 < N:
            x -= 1
            tmp = D[0]
            D[0], D[4], D[5] = D[5], D[2], D[4]
            process(tmp)
    elif opMap[o] == "SOUTH":
        if 0 <= x + 1 < N:
            x += 1
            tmp = D[4]
            D[0], D[4], D[5] = D[2], D[5], D[0]
            process(tmp)
