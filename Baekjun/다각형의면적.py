import sys


def find_area(lst):
    area = 0
    for i in range(len(lst)-1):
        p1 = (lst[i][0] - lst[0][0], lst[i][1] - lst[0][1])
        p2 = (lst[i+1][0] - lst[0][0], lst[i+1][1] - lst[0][1])

        area += (p1[0] * p2[1] - p2[0] * p1[1])/2

    return round(abs(area), 1)


n = int(sys.stdin.readline())
xy = []

for _ in range(n):
    xy.append(list(map(int, input().split())))

print(find_area(xy))
