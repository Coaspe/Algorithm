li = [list(map(int, input().split())) for _ in range(2)]
a, b, c, d = li[0][:2], li[0][2:], li[1][:2], li[1][2:]


def ccw(x1, y1, x2, y2, x3, y3):
    c = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    return 0 if c == 0 else c // abs(c)


l1 = ccw(*a, *b, *c) * ccw(*a, *b, *d)
l2 = ccw(*c, *d, *a) * ccw(*c, *d, *b)

if not l1 and not l2:
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c
    print(1 if a <= d and c <= b else 0)
else:
    print(1 if l1 <= 0 and l2 <= 0 else 0)
