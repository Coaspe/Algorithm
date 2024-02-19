from sys import stdin


input = stdin.readline
N, M = map(int, input().split())

arr = [int(input()) for _ in range(N)]
n = len(arr)
tree = [0] * (n * 2)

for i in range(n):
    tree[n + i] = arr[i]

for i in range(n - 1, 0, -1):
    tree[i] = min(tree[i << 1], tree[i << 1 | 1])


def query(l, r, n):
    res = 1_000_000_000

    l += n
    r += n

    while l < r:
        if l & 1:
            res = min(res, tree[l])
            l += 1

        if r & 1:
            r -= 1
            res = min(res, tree[r])

        l >>= 1
        r >>= 1

    return res


for _ in range(M):
    a, b = map(int, input().split())
    print(query(a - 1, b, n))
