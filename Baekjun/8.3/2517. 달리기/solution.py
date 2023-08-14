from collections import defaultdict
import math


class ST:
    def __init__(self, tree):
        self.tree = tree

    def build(self, arr, n):
        # insert leaf nodes in tree
        for i in range(n):
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


N = int(input())

nums = [int(input()) for _ in range(N)]
nums_s = list(set(nums))

nums_s.sort()

mapping = defaultdict(int)

for i in range(len(nums_s)):
    mapping[nums_s[i]] = i

tree_size = 2 ** math.ceil(math.log2(len(nums_s)))
tree = [0] * 2 * tree_size

st = ST(tree)

for num in nums:
    larger = st.query(mapping[num], len(nums_s), tree_size)
    print(larger + 1)
    st.updateTreeNode(mapping[num], 1, tree_size)
