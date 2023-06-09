from typing import List
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key=lambda x: x[1])
        slots2.sort(key=lambda x: x[1])
        
        p1, p2 = 0, 0

        while p1 <= len(slots1) - 1 and p2 <= len(slots2) - 1:

            start, end = max(slots1[p1][0], slots2[p2][0]), min(slots1[p1][1], slots2[p2][1])

            if end - start >= duration:
                return [start, start + duration]

            if end == slots1[p1][1]:
                p1 += 1
            else:
                p2 += 1
        
        return []
