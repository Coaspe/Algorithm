N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

# 0 - 왼 1 - 아래 2 - 오른 3 - 위


def next_point(r, c, d):
    if d == 0:
        return (r, c-1)
    elif d == 1:
        return (r+1, c)
    elif d == 2:
        return (r, c+1)
    elif d == 3:
        return (r-1, c)


d0 = [
    [0, 0, 0.02, 0, 0],
    [0, 0.1, 0.07, 0.01, 0],
    [0.05, 0, -1, 0, 0],
    [0, 0.1, 0.07, 0.01, 0],
    [0, 0, 0.02, 0, 0]
]
d1 = [[0] * 5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        d1[5 - j - 1][i] = d0[i][j]

d2 = [[0] * 5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        d2[5 - j - 1][i] = d1[i][j]

d3 = [[0] * 5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        d3[5 - j - 1][i] = d2[i][j]

dtomap = {
    0: d0,
    1: d1,
    2: d2,
    3: d3
}
ans = 0


def send_sand(r, c, d):
    global ans
    val = A[r][c]
    board = dtomap[d]
    flew = 0
    for row in range(-2, 3):
        for col in range(-2, 3):
            r_new, c_new, v_new = r+row, c + \
                col, int(board[row+2][col+2] * val)
            flew += v_new * int(v_new > 0)
            if 0 <= r_new < N and 0 <= c_new < N:
                A[r_new][c_new] += v_new
            else:
                ans += v_new
    r1, c1 = next_point(r, c, d)
    if 0 <= r1 < N and 0 <= c1 < N:
        A[r1][c1] += (val-flew)
    else:
        ans += (val-flew)


T = (N//2, N//2)
D = 0
step = (2, 0)
while T != (0, 0):
    T = next_point(T[0], T[1], D)
    # 흩날리기
    send_sand(T[0], T[1], D)
    step = (step[0], step[1] + 1)

    if step[0] / 2 == step[1]:
        D += 1
        D %= 4
    elif step[0] == step[1]:
        D += 1
        D %= 4
        step = (step[0]+2, 0)
print(ans)
