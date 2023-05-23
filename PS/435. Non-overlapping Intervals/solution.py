class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0

        intervals.sort(key=lambda x: x[1])
        prev = intervals[0][1]

        for idx in range(1, len(intervals)):
            if intervals[idx][0] >= prev:
                prev = intervals[idx][1]
            else:
                count += 1

        return count
