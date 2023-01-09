import 'dart:math';

class Solution {
  int longestOnes(List<int> nums, int k) {
      var left = 0, right = 0;
      var answer = 0;
      var numOfZero = 0;

      while (right < nums.length) {
        if (nums[right] == 0) numOfZero += 1;

        while (numOfZero > k) {
          if (nums[left] == 0) numOfZero -= 1;
          left += 1;
        }

        answer = max(answer, right - left + 1);
        right += 1;
      }

      return answer;
  }
}