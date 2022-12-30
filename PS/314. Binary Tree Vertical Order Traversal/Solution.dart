import 'dart:collection';

class TreeNode {
  const TreeNode([this.val = 0, this.left, this.right]);
  final int val;
  final TreeNode? left;
  final TreeNode? right;

  @override
  bool operator ==(o) =>
      identical(o, this) ||
      (o is TreeNode && o.val == val && o.left == left && o.right == right);

  @override
  int get hashCode => Object.hash(val, left, right);
}

class Tuple {
  const Tuple(this.column, this.node);
  final int column;
  final TreeNode? node;

  @override
  bool operator ==(o) =>
      identical(o, this) ||
      (o is Tuple && o.node == node && o.column == column);

  @override
  int get hashCode => Object.hash(node, column);
}

class Solution {
  List<List<int>> verticalOrder(TreeNode? root) {
    Queue queue = Queue<Tuple>();
    queue.add(Tuple(0, root));

    Map dic = <int, List>{};

    while (queue.isNotEmpty) {
      Tuple t = queue.removeLast();

      if (t.node != null) {
        if (!dic.containsKey(t.column)) {
          dic[t.column] = [];
        }

        dic[t.column].add(t.node!.val);

        if (t.node!.left != null) {
          queue.addFirst(Tuple(t.column - 1, t.node!.left));
        }
        if (t.node!.right != null) {
          queue.addFirst(Tuple(t.column + 1, t.node!.right));
        }
      }
    }

    List keys = dic.keys.toList();
    keys.sort();

    return [for (var i in keys) dic[i]];
  }
}
