# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    answer = 0

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        # return value (sum of node.val, count)
        def dfs(node):
            if not node:
                return (0, 0)

            left = dfs(node.left)
            right = dfs(node.right)

            if (left[0] + right[0] + node.val) // (left[1]+right[1]+1) == node.val:
                self.answer += 1

            return (left[0] + right[0] + node.val, left[1]+right[1]+1)
        dfs(root)
        return self.answer
