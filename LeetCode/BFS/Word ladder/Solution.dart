import 'dart:collection';

class Solution {
  int ladderLength(String beginWord, String endWord, List<String> wordList) {
    if (!wordList.contains(endWord)) {
      return 0;
    }
    var allComboDict = <String, List>{};
    for (var word in wordList) {
      for (var i = 0; i <= beginWord.length - 1; i++) {
        var key = word.substring(0, i) + "*" + word.substring(i + 1);
        if (!allComboDict.containsKey(key)) {
          allComboDict[key] = [];
        }
        allComboDict[key]?.add(word);
      }
    }

    var queue = Queue<List<dynamic>>();
    queue.add([beginWord, 1]);

    var visited = {beginWord: true};

    while (queue.isNotEmpty) {
      var wordInfo = queue.removeFirst();
      for (var i = 0; i <= beginWord.length - 1; i++) {
        var intermediateWord =
            wordInfo[0].substring(0, i) + "*" + wordInfo[0].substring(i + 1);
        if (allComboDict.containsKey(intermediateWord)) {
          for (var word in allComboDict[intermediateWord]!) {
            if (word == endWord) {
              return wordInfo[1] + 1;
            }
            if (!visited.containsKey(word)) {
              visited[word] = true;
              queue.add([word, wordInfo[1] + 1]);
            }
          }
          allComboDict[intermediateWord] = [];
        }
      }
    }
    return 0;
  }
}
