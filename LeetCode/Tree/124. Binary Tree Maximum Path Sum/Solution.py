# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer = -math.inf
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def explore(node):
            if not node:
                return 0
            
            left = explore(node.left)
            right = explore(node.right)
            
            self.answer = max(self.answer, left + right + node.val,
            node.val, max(left, right) + node.val)

            return max(max(left, right) + node.val, node.val)

        explore(root)

        return self.answer