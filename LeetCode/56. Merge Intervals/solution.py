from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(reverse=True)
        ans = [intervals.pop()]
        while intervals:
            a, b = intervals.pop()
            c, d = ans.pop()
            if a <= d:
                ans.append([c, max(b, d)])
            else:
                ans.append([c, d])
                ans.append([a, b])
        return ans
