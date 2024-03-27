class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        p = 1
        ans = 0

        for r in range(len(nums)):
            p *= nums[r]

            while l <= r and p >= k:
                p /= nums[l]
                l += 1

            ans += r - l + 1

        return ans
