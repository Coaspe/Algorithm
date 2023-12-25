from bisect import bisect_right


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        dp = []
        ans = []
        for o in obstacles:
            idx = bisect_right(dp, o)

            if idx == len(dp):
                dp.append(o)
                ans.append(len(dp))
            else:
                dp[idx] = o
                ans.append(idx + 1)

        return ans
