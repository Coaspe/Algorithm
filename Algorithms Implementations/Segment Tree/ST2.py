from typing import List


class Solution:
    def build(arr, n, tree):
        for i in range(n):
            tree[n+i] = arr[i]

        for i in range(n-1, 0, -1):
            tree[i] = tree[i << 1] + tree[i << 1 | 1]

    # implement segment tree
    def update(index, value, tree):
        tree[index] += value

        while index > 1:
            index //= 2
            tree[index] = tree[index * 2] + tree[index * 2 + 1]

    def query(left, right, tree, n):
        result = 0
        left += n
        right += n

        while left < right:
            if left % 2 == 1:
                result += tree[left]
                left += 1
            left //= 2

            if right % 2 == 1:
                right -= 1
                result += tree[right]
            right //= 2
            print(left, right)
        return result

    arr = [2, 3, 5, 1, 2, 4, 3]
    size = len(arr)
    tree = [0] * (2 * size)

    build(arr, size, tree)
    print(tree)
    print(query(1, 6, tree, size))
