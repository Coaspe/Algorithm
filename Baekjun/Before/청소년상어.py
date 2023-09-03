M = [[(0, 0)] * 4 for _ in range(4)]

for r in range(4):
    fish = list(map(int, input().split()))
    for c in range(0, len(fish), 2):
        # (number, direction)
        M[r][c//2] = (fish[c], fish[c+1])

ans = 0


def get_points(r, c, d):
    if d == 1:
        return [(r-i, c) for i in range(1, 4) if r-i >= 0]
    elif d == 2:
        return [(r-i, c-i) for i in range(1, 4) if r-i >= 0 and c-i >= 0]
    elif d == 3:
        return [(r, c-i) for i in range(1, 4) if c-i >= 0]
    elif d == 4:
        return [(r+i, c-i) for i in range(1, 4) if r+i < 4 and c-i >= 0]
    elif d == 5:
        return [(r+i, c) for i in range(1, 4) if r+i < 4]
    elif d == 6:
        return [(r+i, c+i) for i in range(1, 4) if r+i < 4 and c+i < 4]
    elif d == 7:
        return [(r, c+i) for i in range(1, 4) if c+i < 4]
    elif d == 8:
        return [(r-i, c+i) for i in range(1, 4) if r-i >= 0 and c+i < 4]
    return []


def get_point(r, c, d):
    if d == 1:
        return (r-1, c)
    elif d == 2:
        return (r-1, c-1)
    elif d == 3:
        return (r, c-1)
    elif d == 4:
        return (r+1, c-1)
    elif d == 5:
        return (r+1, c)
    elif d == 6:
        return (r+1, c+1)
    elif d == 7:
        return (r, c+1)
    elif d == 8:
        return (r-1, c+1)


def move_fish(MAP, shark):

    ar = [(-1, -1)]*17
    for r in range(4):
        for c in range(4):
            if MAP[r][c][0]:
                ar[MAP[r][c][0]] = (r, c)

    indice = [idx for idx, val in enumerate(ar) if val[0] != -1]

    for idx in indice:
        r = c = -1
        for h in range(4):
            if r != -1:
                break
            for w in range(4):
                if idx == MAP[h][w][0]:
                    r, c = h, w
                    break

        new_d = MAP[r][c][1]

        for _ in range(8):
            new_r, new_c = get_point(r, c, new_d)
            if 0 <= new_r < 4 and 0 <= new_c < 4 and (new_r, new_c) != (shark[0], shark[1]):
                MAP[r][c] = (MAP[r][c][0], new_d)
                MAP[r][c], MAP[new_r][new_c] = MAP[new_r][new_c], MAP[r][c]
                break
            else:
                new_d = (new_d + 1) % 9 + (1 if new_d + 1 == 9 else 0)


def move_shark(tmp_sum, MAP, shark):
    global ans
    ans = max(ans, tmp_sum)
    move_fish(MAP, shark)

    points = get_points(*shark)
    for r, c in points:
        if MAP[r][c] != (0, 0):
            o = [i[:] for i in MAP]
            o[r][c] = (0, 0)
            move_shark(tmp_sum + MAP[r][c][0], o, (r, c, MAP[r][c][1]))


ans = 0
first = M[0][0][0]
shark = (0, 0, M[0][0][1])
M[0][0] = (0, 0)
move_fish(M, shark)
points = get_points(*shark)

for r, c in points:
    if M[r][c] != (0, 0):
        tmp = M[r][c]
        o = [i[:] for i in M]
        o[r][c] = (0, 0)
        move_shark(first + M[r][c][0], o, (r, c, M[r][c][1]))

print(ans)
