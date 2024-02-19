from sys import stdin

input = stdin.readline
N, Q = map(int, input().split())
arr = list(map(int, input().split()))
n = len(arr)
tree = [0] * n * 2

for i in range(n):
    tree[n + i] = arr[i]

for i in range(n - 1, 0, -1):
    tree[i] = tree[i << 1] + tree[i << 1 | 1]


def query(l, r):
    ans = 0
    r += n
    l += n

    while r > l:
        if l & 1:
            ans += tree[l]
            l += 1

        if r & 1:
            r -= 1
            ans += tree[r]

        l >>= 1
        r >>= 1

    return ans


def update(idx, v):
    i = idx + n

    tree[i] = v

    while i > 1:
        tree[i >> 1] = tree[i] + tree[i ^ 1]
        i >>= 1


for _ in range(Q):
    x, y, a, b = map(int, input().split())
    print(query(min(x, y) - 1, max(x, y)))
    update(a - 1, b)
