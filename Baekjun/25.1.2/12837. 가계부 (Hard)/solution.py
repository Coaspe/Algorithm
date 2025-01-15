from sys import stdin

input = stdin.readline


class ST:
    def build(self, arr, n, tree):
        for i in range(n):
            tree[n + i] = arr[i]

        for i in range(n - 1, 0, -1):
            tree[i] = tree[i << 1] + tree[i << 1 | 1]

    # implement segment tree
    def update(self, index, value, tree):
        tree[index] += value

        while index > 1:
            index //= 2
            tree[index] = tree[index * 2] + tree[index * 2 + 1]

    def query(self, left, right, tree, n):
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
        return result


st = ST()

N, Q = map(int, input().split())
N += 1
tree = [0] * (2 * N)


for _ in range(Q):
    q, p, x = map(int, input().split())
    if q == 1:
        st.update(p + N, x, tree)
    else:
        print(st.query(p, x + 1, tree, N))
