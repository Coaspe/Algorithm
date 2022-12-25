"""
https://leetcode.com/problems/rearrange-string-k-distance-apart/description/
문자열 s와 정수 k가 주어진다.
같은 문자가 적어도 k 거리만큼 떨어지도록 s를 재정렬하세요.
"""
import collections
import heapq


class Solution:

    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            k = 1
        total = len(s)
        counter = collections.Counter(s)
        res, heap = "", []

        for w, v in counter.items():
            heapq.heappush(heap, (-v, w))

        while len(res) < len(s):
            y = []
            for _ in range(min(k, total)):
                if not len(heap):
                    return ""
                x = heapq.heappop(heap)
                res += x[1]
                if x[0]+1:
                    y.append((x[0]+1, x[1]))
                total -= 1
            for i in y:
                heapq.heappush(heap, i)

        return res
