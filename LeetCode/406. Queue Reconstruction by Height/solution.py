import heapq
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        q = []

        for h, k in people:
            heapq.heappush(q, (-h, k))

        ans = []

        while q:
            h, k = heapq.heappop(q)
            ans.insert(k, [-h, k])

        return ans
