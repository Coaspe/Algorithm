class Solution:
    answer = 0
    def pathSum(self, root: TreeNode, target: int) -> int:
        def preorder(node: TreeNode, curr_sum) -> None:
            if not node:
                return 
            
            curr_sum += node.val
            if curr_sum == target:
                self.answer += 1
            
            self.answer += h[curr_sum - target]

            h[curr_sum] += 1

            preorder(node.left, curr_sum)
            preorder(node.right, curr_sum)

            h[curr_sum] -= 1

        h = defaultdict(int)
        preorder(root, 0)

        return self.answer
    