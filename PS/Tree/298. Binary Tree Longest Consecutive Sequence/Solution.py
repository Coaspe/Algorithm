from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    answer = 0

    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(node, length):
            self.answer = max(self.answer, length)
            if node.left:
                if node.left.val == node.val + 1:
                    dfs(node.left, length + 1)
                else:
                    dfs(node.left, 1)
            if node.right:
                if node.right.val == node.val + 1:
                    dfs(node.right, length + 1)
                else:
                    dfs(node.right, 1)

        dfs(root, 1)
        return self.answer
