class Solution:
    first, last = None, None

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def helper(node):
            if node:
                helper(node.left)

                if self.last:
                    self.last.right = node
                    node.left = self.last
                else:
                    self.first = node
                self.last = node
                helper(node.right)

        if not root:
            return None
        helper(root)

        self.last.right = self.first
        self.first.left = self.last
        return self.first
