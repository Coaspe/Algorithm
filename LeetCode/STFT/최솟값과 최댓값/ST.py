import sys
import math
input = sys.stdin.readline
N, M = map(int, input().split())


def buildMin(arr, n, tree):
    for i in range(n):
        tree[n+i] = arr[i]

    for i in range(n-1, 0, -1):
        tree[i] = min(tree[i << 1], tree[i << 1 | 1])


def buildMax(arr, n, tree):
    for i in range(n):
        tree[n+i] = arr[i]

    for i in range(n-1, 0, -1):
        tree[i] = max(tree[i << 1], tree[i << 1 | 1])


def query(left, right, treeMax, treeMin, n):
    hi, lo = -math.inf, math.inf
    left += n
    right += n

    while left < right:
        if left % 2 == 1:
            hi, lo = max(hi, treeMax[left]), min(lo, treeMin[left])
            left += 1
        left //= 2

        if right % 2 == 1:
            right -= 1
            hi, lo = max(hi, treeMax[right]), min(lo, treeMin[right])
        right //= 2
    return (lo, hi)


arr = [int(input()) for _ in range(N)]
size = len(arr)
min_tree = [0] * (size * 2)
max_tree = [0] * (size * 2)

buildMin(arr, size, min_tree)
buildMax(arr, size, max_tree)

for _ in range(M):
    a, b = map(int, input().split())
    print(*query(a-1, b, max_tree, min_tree, size))
