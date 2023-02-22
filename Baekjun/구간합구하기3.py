def sum(x, y):
    ans = 0
    while x > 0:
        j = y
        while j > 0:
            ans += tree[x][j]
            j -= (j & -j)
        x -= (x & -x)
    return ans


def update(x, y, diff):
    while x <= N:
        j = y
        while j <= N:
            tree[x][j] += diff
            j += (j & -j)
        x += (x & -x)


N, M = map(int, input().split())

mat = [[0]*(N+1) for _ in range(N+1)]
tree = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    tmp = list(map(int, input().split()))
    for j in range(1, N+1):
        mat[i][j] = tmp[j-1]
        update(i, j, tmp[j-1])

for _ in range(M):
    w, *rest = map(int, input().split())
    if w:
        ans = 0
        a, b, c, d = rest
        ans += sum(c, d)
        ans += sum(a-1, b-1)
        ans -= sum(a-1, d)
        ans -= sum(c, b-1)
        print(ans)
    else:
        x, y, c = rest
        update(x, y, c - mat[x][y])
        mat[x][y] = c
