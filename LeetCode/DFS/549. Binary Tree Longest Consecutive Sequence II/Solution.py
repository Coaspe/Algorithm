class Solution:
    answer = 0

    def longestConsecutive(self, root: TreeNode) -> int:

        def longest_path(node: TreeNode) -> Tuple[int, int]:
            if not node:
                return (0, 0)
            icr = dcr = 1
            if node.left:
                left = longest_path(node.left)
                if node.left.val == node.val+1:
                    icr = left[0]+1
                if node.left.val + 1 == node.val:
                    dcr = left[1]+1

            if node.right:
                right = longest_path(node.right)
                if node.right.val == node.val+1:
                    icr = max(icr, right[0]+1)
                if node.right.val+1 == node.val:
                    dcr = max(dcr, right[1]+1)

            self.answer = max(self.answer, icr+dcr-1)

            return [icr, dcr]
        longest_path(root)
        return self.answer
