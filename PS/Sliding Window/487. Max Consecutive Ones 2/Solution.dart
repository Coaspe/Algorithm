import 'dart:math';

class Solution {
  int findMaxConsecutiveOnes(List<int> nums) {
    int l = 0, r = 0;
    int numOfZero = 0, longest = 0;

    while (r <= nums.length - 1) {
      if (nums[r] == 0) {
        numOfZero += 1;
      }
      while (numOfZero >= 2) {
        if (nums[l] == 0) {
          numOfZero -= 1;
        }
        l += 1;
      }
      longest = max(longest, r - l + 1);
      r += 1;
    }
    return longest;
  }
}
