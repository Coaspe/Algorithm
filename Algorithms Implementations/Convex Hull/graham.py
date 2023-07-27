def cross(p1, p2, p3):
    return (p2[0] - p1[0])*(p3[1] - p1[1]) - (p2[1] - p1[1])*(p3[0] - p1[0])


N = int(input())


def slope(p1, p2):
    return 1.0*(p1[1]-p2[1])/(p1[0]-p2[0]) if p1[0] != p2[0] else float('inf')


points = [tuple(map(int, input().split())) for _ in range(N)]

start = min(points)

points.pop(points.index(start))

points.sort(key=lambda p: (slope(p, start), p[0], p[1]))

ans = [start]

for p in points:
    while len(ans) >= 2 and (cross(ans[-2], ans[-1], p) <= 0):
        ans.pop()
    ans.append(p)


print(len(ans))
