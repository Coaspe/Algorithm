N = int(input())
parent = [i for i in range(N)]


def find(x):
    while x != parent[x]:
        x = parent[x]
    return x


def union(p, c):
    p = find(p)
    c = find(c)
    if p != c:
        parent[c] = p

def isCrossed(i, j):
    x1, y1, x2, y2 = points[i]
    x3, y3, x4, y4 = points[j]

    if x3 > x2 or x4 < x1 or y3 > y2 or y4 < y1:
        return False
    if x1 < x3 and x4 < x2 and y1 < y3 and y4 < y2:
        return False
    if x3 < x1 and x2 < x4 and y3 < y1 and y2 < y4:
        return False
    return True

points = [tuple(map(lambda x: int(x)+500, input().split())) for _ in range(N)]

for i in range(N-1):
    for j in range(i+1, N):
        if isCrossed(i, j):
            union(j, i)

for i in range(N):
    r1, c1, r2, c2 = points[i]
    if ((r1 == 500 or r2 == 500) and c1 <= 500 and c2 >= 500) or \
            ((c1 == 500 or c2 == 500) and r1 <= 500 and r2 >= 500):
        parent[find(i)] = -1

parent = set([find(i) for i in range(N)])
ans = 0

for i in parent:
    if i != -1:
        ans += 1
print(ans)
