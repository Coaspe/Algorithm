from typing import List, Dict, Tuple
from collections import defaultdict

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# i 번째 말의 위치
info: List[int] = [-1] * K

# (r, c) 위치에 쌓여 있는 말들의 index
# 위치 : [indices]
file: Dict[Tuple, List[int]] = {}

for i in range(K):
    r, c, d = map(int, input().split())

    info[i] = (r, c, d)

    if (r, c) in file:
        file[(r, c)].append(i)
    else:
        file[(r, c)] = [i]


def next_p(r: int, c: int, d: int):
    if d == 0:
        c += 1
    elif d == 1:
        r -= 1
    elif d == 2:
        c -= 1
    elif d == 3:
        r += 1
    return (r, c)


def move_white(prev: Tuple[int, int], next: Tuple[int, int], move_p: int):
    prev_f, next_f = file[prev] if prev in file else [
    ], file[next] if next in file else []
    move_i = prev_f.index(move_p)
    prev_f = prev_f[:move_i]
    prev_f2 = prev_f[move_i:]
    for i in prev_f2:
        info[i] = (*next, info[i][2])
    next_f.extend(prev_f2)


def move_red(prev: Tuple[int, int], next: Tuple[int, int], move_p: int):
    prev_f, next_f = file[prev] if prev in file else [
    ], file[next] if next in file else []
    move_i = prev_f.index(move_p)
    prev_f = prev_f[:move_i]
    prev_f2 = prev_f[move_i::-1]
    for i in prev_f2:
        info[i] = (*next, info[i][2])
    next_f.extend(prev_f2)
    if len(file[prev]) == 0:
        del file[prev]
    # if len(file[])


def move_blue(cur: Tuple[int, int], d: int):
    for i in file(cur):
        info[i] = (info[i][0], info[i][1], abs(d-2))


while True:
    for i in range(K):
        r1, c1, d = info[i]
        r2, c2 = next_p(r1, c1, d)

        # White
        if board[r2][c2] == 0:
            move_white((r1, c1), (r2, c2), i)
        # Red
        elif board[r][c] == 1:
            move_red((r1, c1), (r2, c2), i)
        # Blue
        elif board[r][c] == 2:
            move_blue(d)
