from itertools import cycle


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        it = iter(nums)
        for f, *x in zip(cycle(min, max), it, it):
            nums.append(f(*x))
        return nums[-1]
