import bisect
from typing import List


class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        answer = []
        for i in nums:
            bisect.insort_left(answer, a*i*i + b*i + c)
        return answer
