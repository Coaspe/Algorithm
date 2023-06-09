import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
re = int(1e9+7)


def build(arr, n, tree):
    for i in range(n):
        tree[n+i] = arr[i]

    for i in range(n-1, 0, -1):
        tree[i] = (tree[i << 1] * tree[i << 1 | 1]) % re


def update(index, value, tree, n):
    index += n
    tree[index] = value

    while index > 1:
        index //= 2
        tree[index] = (tree[index * 2] * tree[index * 2 + 1]) % re


def query(left, right, tree, n):
    result = 1
    left += n
    right += n

    while left < right:
        if left % 2 == 1:
            result *= tree[left]
            result %= re
            left += 1
        left //= 2

        if right % 2 == 1:
            right -= 1
            result *= tree[right]
            result %= re
        right //= 2

    return result


arr = [int(input()) for _ in range(N)]
size = len(arr)
tree = [0] * (size * 2)

build(arr, size, tree)

for _ in range(M+K):
    op, a, b = map(int, input().split())
    if op == 1:
        update(a-1, b, tree, size)
    elif op == 2:
        print(query(a-1, b, tree, size) % re)
