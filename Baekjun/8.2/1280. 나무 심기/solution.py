import math


class ST:
    def __init__(self, tree):
        self.tree = tree

    def build(self, arr, n, nn):
        for i in range(nn):
            self.tree[n + i] = arr[i]

        for i in range(n - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def updateTreeNode(self, p, value, n):
        i = p + n
        self.tree[i] += value
        while i > 1:
            self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]
            i >>= 1

    def query(self, l, r, n):
        res = 0

        l += n
        r += n

        while l < r:
            if l & 1:
                res += self.tree[l]
                l += 1

            if r & 1:
                r -= 1
                res += self.tree[r]

            l >>= 1
            r >>= 1

        return res


MAX = 200_000
N = int(input())

tree_size = 2 ** math.ceil(math.log2(MAX))
tree = [0] * 2 * tree_size
tree2 = [0] * 2 * tree_size


MOD = 1_000_000_007

st = ST(tree)
st2 = ST(tree2)

ans = 1
first = int(input())
st.updateTreeNode(first, 1, tree_size)
st2.updateTreeNode(first, first, tree_size)

for i in range(1, N):
    a = int(input())
    smallers = st.query(0, a, tree_size)
    largers = st.query(a + 1, MAX, tree_size)

    ans *= (
        smallers * a
        - st2.query(0, a, tree_size)
        + st2.query(a + 1, MAX, tree_size)
        - largers * a
    )

    st.updateTreeNode(a, 1, tree_size)
    st2.updateTreeNode(a, a, tree_size)

    ans %= MOD

print(ans)
