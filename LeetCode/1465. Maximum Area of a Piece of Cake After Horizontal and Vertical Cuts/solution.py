from typing import List

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        verticalCuts.append(0)

        horizontalCuts.sort()
        verticalCuts.sort()

        nh = len(horizontalCuts)
        nv = len(verticalCuts)

        h_i = v_i = -1
        
        max_gap = 0

        for idx in range(1, nh):
            if horizontalCuts[idx] - horizontalCuts[idx-1] > max_gap:
                max_gap = horizontalCuts[idx] - horizontalCuts[idx-1] 
                h_i = idx

        max_gap = 0
        for idx in range(1, nv):
            if verticalCuts[idx] - verticalCuts[idx-1] > max_gap:
                max_gap = verticalCuts[idx] - verticalCuts[idx-1] 
                v_i = idx
        
        return (horizontalCuts[h_i]-horizontalCuts[h_i-1]) * (verticalCuts[v_i] - verticalCuts[v_i-1])