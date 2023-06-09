import math


def compress(n):
    arr.sort(key=lambda x: x[1])
    revArr = [0]*n
    rank, prev = -1, math.inf
    for i in range(1, n):
        if prev != arr[i][1]:
            rank += 1
        revArr[arr[i][2]] = (arr[i][0], rank)
        prev = arr[i][1]

    revArr.sort(key=lambda x: (x[0], -x[1]))
    revArr.insert(0, (0, 0))

    return revArr, rank


def update(i, diff, tree):
    while i < len(tree):
        tree[i] += diff
        i += (i & -i)


def sum(i, tree):
    ans = 0
    while i > 0:
        ans += tree[i]
        i -= (i & -i)
    return ans


T = int(input())

for i in range(T):
    arr = []
    n = int(input())

    for j in range(n):
        x, y = map(int, input().split())
        arr.append((x, y, j))

    points, rank = compress(n)
    pl = len(points)
    tree = [0]*pl
    ans = 0

    for i in range(1, pl):
        ans += (sum(rank+1, tree) - sum(points[i][1], tree))
        update(points[i][1]+1, 1, tree)

    print(ans)
