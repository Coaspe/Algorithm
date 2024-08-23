from collections import deque
from sys import stdin

input = stdin.readline
R, C = map(int, input().split())

M = [list(input()) for _ in range(R)]

F = deque()
J = set()

for r in range(R):
    for c in range(C):
        if M[r][c] == "F":
            F.append((r, c))
        elif M[r][c] == "J":
            if r == R - 1 or c == C - 1 or r == 0 or c == 0:
                print(1)
                exit(0)
            J.add((r, c))

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]


def fire():
    new_F = deque()
    global F
    while F:
        r, c = F.popleft()

        for i in range(4):
            row, col = dx[i] + r, dy[i] + c

            if (
                0 <= row < R
                and 0 <= col < C
                and (M[row][col] == "." or M[row][col] == "J")
            ):

                J.discard((row, col))
                end_candid.discard((row, col))

                M[row][col] = "F"
                new_F.append((row, col))
    F = new_F


end_candid = set()


def move_J():
    new_J = set()
    global J
    for r, c in J:
        for i in range(4):
            row, col = dx[i] + r, dy[i] + c

            if 0 <= row < R and 0 <= col < C and M[row][col] == ".":
                new_J.add((row, col))
                M[row][col] = "J"
                if row == R - 1 or row == 0 or col == C - 1 or col == 0:
                    end_candid.add((row, col))
    J = new_J


T = 1
while J:
    T += 1
    move_J()
    fire()

    if end_candid:
        print(T)
        exit(0)

print("IMPOSSIBLE")
