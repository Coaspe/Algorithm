def CCW(p1, p2, p3):
    rst = (p2[0]-p1[0])*(p3[1]-p1[1]) - (p2[1]-p1[1])*(p3[0]-p1[0])

    if rst > 0:
        return 1
    elif rst < 0:
        return -1
    else:
        return 0


x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
p1 = [x1, y1]
p2 = [x2, y2]
p3 = [x3, y3]
p4 = [x4, y4]

ans1 = CCW(p1, p2, p3) * CCW(p1, p2, p4)
ans2 = CCW(p3, p4, p1) * CCW(p3, p4, p2)

if ans1 == ans2 == -1:
    print(1)
else:
    print(0)
