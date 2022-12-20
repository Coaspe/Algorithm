import 'dart:math';

class TreeNode {
  int val;
  TreeNode? left;
  TreeNode? right;
  TreeNode([this.val = 0, this.left, this.right]);
}

class Solution {
  int longestConsecutive(TreeNode? root) {
    int answer = 0;
    void dfs(TreeNode? node, int value) {
      answer = max(answer, value);

      if (node?.left != null) {
        if (node?.left?.val == node!.val + 1) {
          dfs(node.left, value + 1);
        } else {
          dfs(node.left, 1);
        }
      }
      if (node?.right != null) {
        if (node?.right?.val == node!.val + 1) {
          dfs(node.right, value + 1);
        } else {
          dfs(node.right, 1);
        }
      }
    }

    dfs(root, 1);
    return answer;
  }
}
