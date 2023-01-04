class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_far = min_far = answer = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            tmp = max(num, max_far * num, min_far*num)
            min_far = min(num, max_far * num, min_far*num)
            max_far = tmp
            answer = max(answer, max_far)

        return answer