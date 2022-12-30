class SegmentTree:
    def init(self, a, tree, node, start, end):
        if start == end:
            tree[node] = a[start]
        else:
            self.init(a, tree, node*2, start, (start+end)//2)
            self.init(a, tree, node*2+1, (start+end) // 2 + 1, end)
            tree[node] = tree[2*node+1] + tree[2*node]

    def __init__(self, a, tree, node, start, end):
        self.a = a
        self.tree = tree
        self.init(self.a, self.tree, node, start, end)

    def query(self, node, start, end, left, right):
        if left > end or right < start:
            return 0
        if left <= start and end <= right:
            return self.tree[node]

        lsum = self.query(node*2, start, (start+end)//2, left, right)
        rsum = self.query(node*2+1, (start+end)//2 + 1, end, left, right)
        return lsum + rsum

    def update(self, node, start, end, index, val):
        if index < start or index > end:
            return
        if start == end:
            self.a[index] = val
            self.tree[node] = val
            return
        self.update(node*2, start, (start+end)//2, index, val)
        self.update(node*2+1, (start+end)//2+1, end, index, val)
        self.tree[node] = self.tree[node*2] + self.tree[node*2+1]

    # def update_tree(self, node, start, end, index, diff):
    #     if index < start or index> end:
    #         return
    #     self.tree[node] = self.tree[node] + diff
    #     if start != end:
    #         self.update_tree(self.tree, node*2, start, (start+end)//2, index, diff)
    #         self.update_tree(self.tree, node*2+1, (start+end)//2+1, end, index, diff)

    # def update(self, n, index, val):
    #     diff = val - self.a[index]
    #     self.a[index] = val
    #     self.update_tree(1, 0, n-1, index, diff)
