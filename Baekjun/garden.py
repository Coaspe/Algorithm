from itertools import combinations
N, M, G, R = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

fertile = set()
ans = 0

for r in range(N):
    for c in range(M):
        if MAP[r][c] == 2:
            fertile.add((r, c))

# 0 - 호수, 1 - 배양액 x, 2 - 배양액 o
# 3 - green 4 - red 5 - flower
LAKE = 0
NSOLUTION = 1
SOLUTION = 2
GREEN = 3
RED = 4
FLOWER = 5

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def breed(green, red, MAP):
    flower = 0
    MM = [i[:] for i in MAP]
    green = set(green)
    red = set(red)

    for r, c in green:
        MM[r][c] = GREEN

    for r, c in red:
        MM[r][c] = RED

    g_len_tmp = r_len_tmp = ans_tmp = -1

    while g_len_tmp != len(green) or r_len_tmp != len(red) or ans_tmp != flower:
        g_len_tmp, r_len_tmp, ans_tmp = len(green), len(red), flower

        # 그 자리에서 2칸씩 확인해야함
        for r, c in list(green):
            for i in range(4):
                row1, col1 = r+dx[i], c+dy[i]
                if 0 <= row1 < N and 0 <= col1 < M and MM[row1][col1] in [NSOLUTION, SOLUTION]:
                    row2, col2 = row1+dx[i], col1+dy[i]
                    if 0 <= row2 < N and 0 <= col2 < M:
                        if MM[row2][col2] == RED:
                            MM[row1][col1] = FLOWER
                            flower += 1
                        else:
                            MM[row1][col1] = GREEN
                            green.add((row1, col1))
                    else:
                        MM[row1][col1] = GREEN
                        green.add((row1, col1))

        # 빨강 배양액은 한칸씩 확인
        for r, c in list(red):
            for i in range(4):
                row1, col1 = r+dx[i], c+dy[i]
                if 0 <= row1 < N and 0 <= col1 < M and MM[row1][col1] in [NSOLUTION, SOLUTION]:
                    MM[row1][col1] = RED
                    red.add((row1, col1))
    return flower


for green in combinations(fertile, G):
    green = set(green)
    left_fertile = set([x for x in fertile if x not in green])
    for red in combinations(left_fertile, R):
        ans = max(breed(green, red, MAP), ans)

print(ans)
