import sys
input = sys.stdin.readline
n = int(input())
dots = []
dA = dots.append
for _ in range(n):
    x, y, c = input().split()
    if c == 'Y':
        dA([int(x), int(y)])


def ccw(p1, p2, p3):
    return p1[0]*(p2[1] - p3[1]) + p2[0]*(p3[1] - p1[1]) + p3[0]*(p1[1] - p2[1])


def chain(dots):
    dots.sort()

    lower = []
    for d in dots:
        while len(lower) >= 2 and ccw(lower[-2], lower[-1], d) < 0:
            lower.pop()
        lower.append(d)

    upper = []
    for d in reversed(dots):
        while len(upper) >= 2 and ccw(upper[-2], upper[-1], d) < 0:
            upper.pop()
        upper.append(d)
    return lower[:-1] + upper[:-1]


res = chain(dots)
print(len(res))
for x, y in res:
    print(f'{x} {y}')
