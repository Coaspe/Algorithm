import sys
sys.setrecursionlimit(10**5)
N = int(input())


def CCW(a, b, c):
    result = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0]-a[0])
    if result > 0:
        return -1
    elif result < 0:
        return 1
    else:
        return 0


def check(x1, y1, x2, y2, x3, y3, x4, y4):
    ccw1, ccw2 = CCW((x1, y1), (x2, y2), (x3, y3)), CCW(
        (x1, y1), (x2, y2), (x4, y4))
    ccw3, ccw4 = CCW((x3, y3), (x4, y4), (x1, y1)), CCW(
        (x3, y3), (x4, y4), (x2, y2))
    if ccw1 * ccw2 == 0 and ccw3 * ccw4 == 0:
        if min(x1, x2) <= max(x3, x4) and max(x1, x2) >= min(x3, x4) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
            return 1
    elif ccw1 * ccw2 <= 0 and ccw3 * ccw4 <= 0:
        return 1
    return 0


parent = [i for i in range(N)]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(p, c):
    p = find(p)
    c = find(c)

    if p != c:
        if p > c:
            parent[c] = p
            counts[p] += counts[c]
        else:
            parent[p] = c
            counts[c] += counts[p]


points = [tuple(map(int, input().split())) for _ in range(N)]
counts = [1] * N

for i in range(N):
    x1, y1, x2, y2 = points[i]
    for j in range(i+1, N):
        x3, y3, x4, y4 = points[j]
        if check(x1, y1, x2, y2, x3, y3, x4, y4):
            union(i, j)
ans = {}
for i in parent:
    p = find(i)
    ans[p] = counts[p]

print(len(ans))
print(max(ans.values()))
