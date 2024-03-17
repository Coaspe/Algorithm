from collections import defaultdict
from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        top = defaultdict(int)
        btm = defaultdict(int)
        dup = defaultdict(int)

        for i in range(len(tops)):
            if tops[i] == bottoms[i]:
                dup[tops[i]] += 1
            else:
                top[tops[i]] += 1
                btm[bottoms[i]] += 1

        ans = len(tops) + 1

        for key in set(tops):
            if top[key] + btm[key] + dup[key] == len(tops):
                ans = min(ans, btm[key], top[key])

        return ans if ans != len(tops) + 1 else -1
