class Solution {
  bool reachingPoints(int sx, int sy, int tx, int ty) {
    while (tx >= sx && ty >= sy) {
      if (tx > ty) {
        if (ty > sy) {
          tx %= ty;
        } else {
          return (tx - sx) % ty == 0;
        }
      } else if (ty > tx) {
        if (tx > sx) {
          ty %= tx;
        } else {
          return (ty - sy) % tx == 0;
        }
      } else {
        break;
      }
    }
    return (tx == sx && ty == sy);
  }
}
