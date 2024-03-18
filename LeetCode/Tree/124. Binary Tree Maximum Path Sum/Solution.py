# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = root.val

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            val = max(left, right, left + right, 0) + node.val

            nonlocal ans
            ans = max(ans, val)

            return max(left, right, 0) + node.val

        dfs(root)

        return ans
