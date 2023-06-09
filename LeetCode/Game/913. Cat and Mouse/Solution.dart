import 'dart:collection';

class Solution {
  int catMouseGame(List<List<int>> graph) {
    int N = graph.length;

    Iterable<List<int>> parent(int m, int c, int t) sync* {
      if (t == 2) {
        for (var m2 in graph[m]) {
          yield [m2, c, 3 - t];
        }
      } else {
        for (var c2 in graph[c]) {
          if (c2 > 0) {
            yield [m, c2, 3 - t];
          }
        }
      }
    }

    const DRAW = 0, MOUSE = 1, CAT = 2;
    var color = <List, int>{};
    var degree = <List, int>{};

    for (var m = 0; m < N; m++) {
      for (var c = 0; c < N; c++) {
        degree[[m, c, 1]] = graph[m].length;
        degree[[m, c, 2]] = graph[c].length - (graph[c].contains(0) ? 1 : 0);
      }
    }

    var queue = Queue();
    for (var i = 0; i < N; i++) {
      for (var t = 1; t < 3; t++) {
        color[[0, i, t]] = MOUSE;
        queue.add([0, i, t, MOUSE]);
        if (i > 0) {
          color[[i, i, t]] = CAT;
          queue.add([i, i, t, CAT]);
        }
      }
    }

    while (queue.isNotEmpty) {
      var node = queue.removeFirst();
      var i = node[0], j = node[1], t = node[2], c = node[3];
      for (var nextNode in parent(i, j, t)) {
        if (!color.containsKey(nextNode) || color[nextNode] == 0) {
          if (nextNode[2] == c) {
            color[nextNode] = c;
            queue.add([...nextNode, c]);
          } else {
            degree[nextNode] = degree[nextNode]! - 1;
            if (degree[nextNode] == 0) {
              color[nextNode] = 3 - nextNode[2];
              queue.add([...nextNode, 3 - nextNode[2]]);
            }
          }
        }
      }
    }
    print(color);
    return color.containsKey([1, 2, 1]) ? color[[1, 2, 1]]! : 0;
  }
}
