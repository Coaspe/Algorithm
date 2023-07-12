import math


class SegmentTree:
    def init(self, a, tree, node, start, end):
        if start == end:
            tree[node] = a[start]
        else:
            self.init(a, tree, node * 2, start, (start+end) // 2)
            self.init(a, tree, node * 2 + 1, (start+end) // 2 + 1, end)
            tree[node] = min(tree[2 * node + 1], tree[2 * node])

    def __init__(self, a, tree, node, start, end):
        self.a = a
        self.tree = tree
        self.init(self.a, self.tree, node, start, end)

    def query(self, node, start, end, left, right):
        if left > end or right < start:
            return math.inf
        if left <= start and end <= right:
            return self.tree[node]

        lsum = self.query(node*2, start, (start+end) // 2, left, right)
        rsum = self.query(node*2+1, (start+end) // 2 + 1, end, left, right)

        return min(lsum, rsum)

    def update(self, node, start, end, index, val):
        if index < start or index > end:
            return
        if start == end:
            self.a[index] = val
            self.tree[node] = val
            return

        self.update(node*2, start, (start+end)//2, index, val)
        self.update(node*2+1, (start+end)//2+1, end, index, val)
        self.tree[node] = min(self.tree[node*2], self.tree[node*2+1])


N, L = map(int, input().split())
A = list(map(int, input().split()))
h = math.ceil(math.log2(len(A)))
tree_size = 1 << (h+1)
tree = [math.inf]*tree_size
ans = []
st = SegmentTree(A, tree, 1, 0, len(A)-1)

for i in range(N):
    ans.append(st.query(1, 0, N-1, max(0, i-L+1), i))

print(*ans)
