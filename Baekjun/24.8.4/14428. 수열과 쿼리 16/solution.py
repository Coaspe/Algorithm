import sys

input = sys.stdin.readline


def build(tree, arr, n):
    for i in range(n):
        tree[n + i] = i

    for i in range(n - 1, 0, -1):
        tree[i] = min(tree[i << 1], tree[i << 1 | 1], key=lambda x: (arr[x], x))


def update_tree_node(tree, p, n, arr):
    i = p + n

    while i > 1:
        tree[i >> 1] = min(tree[i], tree[i ^ 1], key=lambda x: (arr[x], x))
        i >>= 1


def query(tree, l, r, n, arr):
    res = -1
    l += n
    r += n

    while l < r:
        if l & 1:
            if res == -1:
                res = tree[l]
            else:
                res = min(res, tree[l], key=lambda x: (arr[x], x))
            l += 1

        if r & 1:
            r -= 1
            if res == -1:
                res = tree[r]
            else:
                res = min(res, tree[r], key=lambda x: (arr[x], x))

        l >>= 1
        r >>= 1

    return res


N = int(input())
tree = [0] * 2 * N
arr = list(map(int, input().split()))
ans = []
build(tree, arr, N)

for _ in range(int(input())):
    op, i, vj = map(int, input().split())
    i -= 1
    if op == 1:
        arr[i] = vj
        update_tree_node(tree, i, N, arr)
    else:
        vj -= 1
        ans.append(str(query(tree, i, vj + 1, N, arr) + 1))

print("\n".join(ans))
