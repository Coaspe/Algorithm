from typing import List


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        # nums와 cost를 묶은 리스트 생성
        r, l = max(nums), min(nums)
        combined = list(zip(nums, cost))

        def get_cost(base):
            return sum(abs(base - num) * c for num, c in combined)

        ans = get_cost(l)

        while r > l:
            mid = (r + l) // 2
            c1 = get_cost(mid)
            c2 = get_cost(mid + 1)
            ans = min(c1, c2)

            if c1 > c2:
                l = mid + 1
            else:
                r = mid

        return ans
