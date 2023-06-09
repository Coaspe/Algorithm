# Each node will return min node value, max node value, size
class NodeValue:
    def __init__(self, min_node, max_node, max_size):
        self.max_node = max_node
        self.min_node = min_node
        self.max_size = max_size


class Solution:
    def largest_bst_subtree_helper(self, root):
        if not root:
            return NodeValue(float('inf'), float('-inf'), 0)
        left = self.largest_bst_subtree_helper(root.left)
        right = self.largest_bst_subtree_helper(root.right)

        if left.max_node < root.val < right.min_node:
            return NodeValue(min(root.val, left.min_node), max(root.val, right.max_node),
                             max(left.max_size+right.max_size+1)
                             )

        return NodeValue(float('-inf'), float('inf'), max(left.max_size, right.max_size))

    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        return self.largest_bst_subtree_helper(root).max_size
