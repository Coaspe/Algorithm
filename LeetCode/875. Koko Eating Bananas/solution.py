from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while right > left:
            count = 0
            mid = (right + left) // 2

            for i in piles:
                count += math.ceil(i / mid)

            if h >= count:
                right = mid
            else:
                left = mid + 1

        return right
