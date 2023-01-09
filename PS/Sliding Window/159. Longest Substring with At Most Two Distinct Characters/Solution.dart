import 'dart:math';

class Solution {
  int lengthOfLongestSubstringTwoDistinct(String s) {
      var answer = 0, n = s.length;
      var left = 0, right = 0;
      Map<String, int> added = {};

      while (right < n) {
          added[s[right]] = right;
          if (added.length >= 3){
            var minVal = added.entries.reduce((cur,next) => cur.value < next.value ? cur : next);
            left = minVal.value;
            added.remove(minVal.key);
          }
          answer = max(answer, right - left + 1);
          right += 1;
      }
      
      return answer;
  }
}