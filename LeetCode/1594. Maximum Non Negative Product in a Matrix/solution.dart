import 'dart:math';

class Solution {
  int inf = double.maxFinite.toInt();

  (int, int) dp(int i, int j, List<List<int>> grid) {
    if (i == 0 && j == 0) {
      return (grid.first[0], grid.first[0]);
    }

    if (i < 0 || j < 0) {
      return (-inf, inf);
    }

    var (mx1, mn1) = dp(i - 1, j, grid);
    var (mx2, mn2) = dp(i, j - 1, grid);

    int mx = max(mx1, mx2) * grid[i][j], mn = min(mn1, mn2) * grid[i][j];

    return grid[i][j] > 0 ? (mx, mn) : (mn, mx);
  }

  int maxProductPath(List<List<int>> grid) {
    int m = grid.length, n = grid.first.length;

    var (mx, _) = dp(m - 1, n - 1, grid);

    return mx < 0 ? -1 : (mx % (1e9 + 7)).toInt();
  }
}
