from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1

        ans = 0
        sum = 0

        for n in nums:
            sum += n
            if dic[sum - k]:
                ans += dic[sum - k]
            dic[sum] += 1

        return ans
