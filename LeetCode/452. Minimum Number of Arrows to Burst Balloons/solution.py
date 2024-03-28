class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(reverse=True)

        ans = 1
        end = points.pop()[1]

        while points:
            s, e = points.pop()

            if s > end:
                ans += 1
                end = e
            else:
                end = min(e, end)

        return ans