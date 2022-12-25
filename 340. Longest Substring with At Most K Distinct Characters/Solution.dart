import 'dart:math';

class Solution {
  int lengthOfLongestSubstringKDistinct(String s, int k) {
    if (k == 0) return 0;
    int answer = 0;
    var l = 0, r = 0;
    Map dic = <String, int>{};

    while (r < s.length) {
      if (!dic.containsKey(dic[r])) dic[r] = 0;
      dic[r] += 1;

      while (dic.keys.length > k) {
        dic[l] -= 1;
        if (dic[l] == 0) dic.remove(l);
        l += 1;
      }
      answer = max(answer, r - l + 1);
      r += 1;
    }

    return answer;
  }
}
