import sys
import math

input = sys.stdin.readline
N, M = map(int, input().split())

a = [0] * N
tree_size = math.ceil(math.log2(N)) + 1
tree = [0] * (1 << tree_size)
lazy = [0] * (1 << tree_size)


def init(node, start, end):
    if start == end:
        tree[node] = a[start]
    else:
        init(node * 2, start, (start + end) // 2)
        init(node * 2 + 1, (start + end) // 2 + 1, end)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]


def query(node, start, end, left, right):
    update_lazy(node, start, end)

    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    return query(node * 2, start, (start + end) // 2, left, right) + query(
        node * 2 + 1, (start + end) // 2 + 1, end, left, right
    )


def update_lazy(node, start, end):
    if lazy[node] != 0:
        tree[node] = (end - start + 1) - tree[node]
        if start != end:
            lazy[2 * node] = not lazy[2 * node]
            lazy[2 * node + 1] = not lazy[2 * node + 1]
        lazy[node] = 0


def update(node, start, end, left, right):
    update_lazy(node, start, end)

    if left > end or right < start:
        return

    if left <= start and end <= right:
        tree[node] = (end - start + 1) - tree[node]
        if start != end:
            lazy[node * 2] = not lazy[node * 2]
            lazy[node * 2 + 1] = not lazy[node * 2 + 1]
        return

    update(node * 2, start, (start + end) // 2, left, right)
    update(node * 2 + 1, (start + end) // 2 + 1, end, left, right)

    tree[node] = tree[node * 2] + tree[node * 2 + 1]


for _ in range(M):
    o, s, t = map(int, input().split())

    # query
    if o:
        print(query(1, 0, N - 1, s - 1, t - 1))
    # update
    else:
        update(
            1,
            0,
            N - 1,
            s - 1,
            t - 1,
        )
