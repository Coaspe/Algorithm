class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            n = abs(n)
            if nums[n - 1] < 0:
                ans.append(n)
            nums[n - 1] *= -1
        return ans
