import math


def distance(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return math.sqrt(dx * dx + dy * dy)


n = int(input())
m = min(n, 20)
ps = [list(map(int, input().split())) for _ in range(n)]

dist = [[float("inf")] * m for _ in range(n)]
dist[0][0] = 0

# 마지막으로 방문한 체크포인트
# k - j + 1 -> k , (j - 1 -> i1과 i 사이에 생기는 skip points)
for i in range(1, n):
    for j in range(1, m + 1):
        if i >= j:
            d = distance(ps[i], ps[i - j])
            for k in range(j - 1, min(i, m)):
                dist[i][k] = min(dist[i][k], dist[i - j][k - (j - 1)] + d)

ans = dist[n - 1][0]

for i in range(1, m):
    ans = min(ans, dist[n - 1][i] + (1 << (i - 1)))

print(ans)
