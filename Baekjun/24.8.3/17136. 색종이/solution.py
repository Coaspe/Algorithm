def promise(a1, a2, b1, b2):  # 유망 조건
    for i in range(a1, a2 + 1):
        for j in range(b1, b2 + 1):
            if not paper[i][j]:
                return False
    return True


def attach(a1, a2, b1, b2, w):  # 색종이 붙이기/떼기
    for i in range(a1, a2 + 1):
        for j in range(b1, b2 + 1):
            paper[i][j] = w


def glue(p):
    global result
    for y in range(10):
        for x in range(10):
            if paper[y][x]:
                for c in range(5):
                    ny, nx = y + c, x + c
                    if confetti[c] and ny < 10 and nx < 10:
                        if promise(y, ny, x, nx):
                            attach(y, ny, x, nx, 0)
                            confetti[c] -= 1
                            glue(p + 1)
                            confetti[c] += 1
                            attach(y, ny, x, nx, 1)
                return
    result = min(result, p)


import sys

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
confetti = [5, 5, 5, 5, 5]
result = 26
glue(0)

if result == 26:
    print(-1)
else:
    print(result)
