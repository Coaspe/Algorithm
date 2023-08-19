T = int(input())


class ST:
    def __init__(self, tree):
        self.tree = tree

    def build(self, arr, n):
        # insert leaf nodes in tree
        for i in range(len(arr)):
            self.tree[n + i] = arr[i]

        # build the tree by calculating parents
        for i in range(n - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    # function to update a tree node
    def updateTreeNode(self, p, value, n):
        # set value at position p
        i = p + n
        self.tree[i] += value

        while i > 1:
            self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]
            i >>= 1

    # function to get sum on interval [l, r)
    def query(self, l, r, n):
        res = 0

        # loop to find the sum in the range
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


import math

while T:
    T -= 1
    n, m = map(int, input().split())

    tree_size = 2 ** math.ceil(math.log2(n + m))
    tree = [0] * tree_size * 2
    arr = [0] * m + [1] * n

    dvds = [i + m for i in range(n)]

    st = ST(tree)
    st.build(arr, tree_size)

    Q = list(map(int, input().split()))

    lastest = m - 1
    ans = []

    for q in Q:
        idx = q - 1
        pos = dvds[idx]
        st.updateTreeNode(pos, -1, tree_size)

        ans.append(st.query(0, pos, tree_size))

        dvds[idx] = lastest
        lastest -= 1

        st.updateTreeNode(dvds[idx], 1, tree_size)

    print(*ans)
