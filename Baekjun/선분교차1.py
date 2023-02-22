x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())


def CCW(p1, p2, p3):
    res = (p2[0]-p1[0])*(p3[1]-p1[1]) - (p2[1]-p1[1])*(p3[0]-p1[0])
    if res > 0:
        return -1
    elif res < 0:
        return 1
    return 0


p1 = (x1, y1)
p2 = (x2, y2)
p3 = (x3, y3)
p4 = (x4, y4)
c1 = CCW(p1, p2, p3) * CCW(p1, p2, p4)
c2 = CCW(p3, p4, p1) * CCW(p3, p4, p2)

if c1 == -1 and c2 == -1:
    print(1)
else:
    print(0)
