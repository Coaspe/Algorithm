from typing import List
class Solution:
    def subsets(self, nums: List[int]):
        nums.sort()
        seen = set()
        for mask in range(1 << len(nums)):
            tmp = []
            for i in len(nums):
                bit = (mask >> i) & 1
                if bit:
                    tmp.append(nums[i])
            seen.add(tuple(tmp))
        return seen