class SegmentTree:
    def init(self, a, tree, node, start, end):
        if start == end:
            tree[node] = a[start]
        else:
            self.init(a, tree, node * 2, start, (start+end) // 2)
            self.init(a, tree, node * 2 + 1, (start+end) // 2 + 1, end)
            tree[node] = tree[2 * node + 1] + tree[2 * node]

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

class ST:
    def __init__(self, tree):
        self.tree = tree

    def build(self, arr, n):
        # insert leaf nodes in tree 
        for i in range(n): 
            self.tree[n + i] = arr[i]; 
        
        # build the tree by calculating parents 
        for i in range(n - 1, 0, -1): 
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]
    
    # function to update a tree node 
    def updateTreeNode(self, p, value, n): 
        
        # set value at position p 
        self.tree[p + n] = value; 
        p = p + n
        
        # move upward and update parents 
        i = p
        
        while i > 1 :
            self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]; 
            i >>= 1; 
    
    # function to get sum on interval [l, r) 
    def query(self, l, r, n) : 
    
        res = 0; 
        
        # loop to find the sum in the range 
        l += n
        r += n
        
        while l < r :
        
            if l & 1:
                res += self.tree[l]; 
                l += 1
        
            if r & 1:
                r -= 1
                res += self.tree[r]

                
            l >>= 1
            r >>= 1
        
        return res
        
"""
    Tree Construction: O(n)
    Query in Range: O(Log n)
    Updating an element: O(Log n)
"""

if __name__ == "__main__" : 
  
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]; 
    n = len(a); 
    tree = [0]*(n*2)
    st = ST(tree)

    st.build(a, n); 
      
    print(st.query(1, 10, n)); 
      
    st.updateTreeNode(2, 1, n); 
      
    print(st.query(1, 3, n)); 