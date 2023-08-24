import sys
import math

input = sys.stdin.readline

a = list(map(int, input().split()))
tree_size = math.ceil(math.log2(len(a))) + 1
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

    if left <= start and end <= right:
        return tree[node]
    if left > end or end < start:
        return 0

    return query(node * 2, start, (start + end) // 2, left, right) + query(
        node * 2 + 1, (start + end) // 2, end, left, right
    )


def update_lazy(node, start, end):
    if lazy[node] != 0:
        tree[node] += (end - start + 1) * lazy[node]
        if start != end:
            lazy[2 * node] += lazy[node]
            lazy[2 * node + 1] += lazy[node]
        lazy[node] = 0


def update_range(node, start, end, left, right, val):
    update_lazy(node, start, end)

    if left > end or right < start:
        return

    if left <= start and end <= right:
        tree[node] += (end - start + 1) * val
        if start != end:
            lazy[node * 2] += val
            lazy[node * 2 + 1] += val
        return

    update_range(node * 2, start, (start + end) // 2, left, right, val)
    update_range(node * 2 + 1, (start + end) // 2 + 1, end, left, right, val)

    tree[node] = tree[node * 2] + tree[node * 2 + 1]
