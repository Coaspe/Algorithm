class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        max_v = max(nums)

        acc = ans = 0

        while nums:
            if nums.pop() == max_v:
                acc += 1
                ans = max(ans, acc)
            else:
                acc = 0

        return ans
