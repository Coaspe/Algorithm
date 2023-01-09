class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        num_zero = 0
        answer = 0

        while right < len(nums):
            num_zero += nums[right] == 0

            while num_zero > k:
                num_zero -= nums[left] == 0
                left += 1
            
            answer = max(answer, right - left + 1)
            right += 1

        return answer