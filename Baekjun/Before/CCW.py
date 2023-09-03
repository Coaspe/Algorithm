x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())


def solve():
    S = (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)
    if S > 0:
        return 1
    elif S < 0:
        return -1
    return 0


print(solve())
