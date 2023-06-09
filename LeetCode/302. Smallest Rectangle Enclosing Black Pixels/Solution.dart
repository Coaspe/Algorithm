import 'dart:math';

class Tuple {
  const Tuple(this.x, this.y);
  final x;
  final y;

  @override
  bool operator ==(Object o) {
    if (o is Tuple) {
      return x == o.x && y == o.y;
    }
    return false;
  }

  @override
  int get hashCode => Object.hash(x, y);
}

class Solution {
  int minArea(List<List<String>> image, int x, int y) {
    int maxVal = 9223372036854775807;
    var l1 = maxVal, r1 = 0, t1 = maxVal, b1 = 0;
    var visited = Set();
    var m = image.length, n = image[0].length;

    void dfs(int r, int c) {
      visited.add(Tuple(r, c));
      l1 = min(l1, c);
      r1 = max(r1, c);
      t1 = min(t1, r);
      b1 = max(b1, r);

      for (var point in [
        [r + 1, c],
        [r, c + 1],
        [r - 1, c],
        [r, c - 1]
      ]) {
        if (0 <= point[0] &&
            point[0] <= m - 1 &&
            0 <= point[1] &&
            point[1] <= n - 1 &&
            image[point[0]][point[1]] == "1" &&
            !visited.contains(point)) {
          dfs(point[0], point[1]);
        }
      }
    }

    dfs(x, y);
    return ((l1 - r1).abs() + 1) * ((t1 - b1).abs() + 1);
  }
}
