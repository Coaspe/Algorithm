import itertools
from typing import List


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        arr.sort(reverse=True)

        for a, b, c, d in itertools.permutations(range(4)):
            a, b, c, d = arr[a], arr[b], arr[c], arr[d]

            if (
                (a > 2)
                or (a == 2 and b > 4)
                or (a == 2 and b == 4 and (c != 0 or b != 0))
                or c >= 6
            ):
                continue

            return f"{a}{b}:{c}{d}"
        return ""
