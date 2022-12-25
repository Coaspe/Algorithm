class TreeNode {
  int val;
  TreeNode? left;
  TreeNode? right;
  TreeNode([this.val = 0, this.left, this.right]);
}

class Tuple {
  final int sumOfVal;
  final int sumOfCount;

  const Tuple(this.sumOfVal, this.sumOfCount);

  @override
  bool operator ==(o) =>
      identical(o, this) ||
      o is Tuple && o.sumOfCount == sumOfCount && o.sumOfVal == sumOfVal;

  @override
  int get hashCode => Object.hash(sumOfVal, sumOfCount);
}

class Solution {
  int answer = 0;
  int averageOfSubtree(TreeNode? root) {
    Tuple dfs(TreeNode? node) {
      if (node == null) return const Tuple(0, 0);
      Tuple left = dfs(node.left);
      Tuple right = dfs(node.right);
      int sumVal = left.sumOfVal + right.sumOfCount + node.val;
      int sumCount = left.sumOfCount + right.sumOfCount + 1;
      if (sumVal / sumCount == node.val) {
        answer += 1;
      }
      return Tuple(sumVal, sumCount);
    }

    dfs(root);
    return answer;
  }
}
