class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r = 0, 0
        numOfZero = 0
        longest = 0
        while r <= len(nums) - 1:
            if nums[r] == 0:
                numOfZero += 1

            while numOfZero >= 2:
                if nums[l] == 0:
                    numOfZero -= 1
                l += 1
            longest = max(longest, r - l + 1)
            r += 1
        return longest
