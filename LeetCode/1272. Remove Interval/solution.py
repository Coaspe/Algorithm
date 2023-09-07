from typing import List


class Solution:
    def removeInterval(
        self, intervals: List[List[int]], toBeRemoved: List[int]
    ) -> List[List[int]]:
        remove_start, remove_end = toBeRemoved
        output = []

        for start, end in intervals:
            # If there are no overlaps, add the interval to the list as is.
            if start > remove_end or end < remove_start:
                output.append([start, end])
            else:
                # Is there a left interval we need to keep?
                if start < remove_start:
                    output.append([start, remove_start])
                # Is there a right interval we need to keep?
                if end > remove_end:
                    output.append([remove_end, end])

        return output
