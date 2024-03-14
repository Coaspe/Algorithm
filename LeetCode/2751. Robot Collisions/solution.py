from typing import List


class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:

        N = len(positions)
        directions = list(directions)
        positions = [(positions[i], i) for i in range(N)]
        positions.sort()

        stack = []

        for idx in range(N):
            i = positions[idx][1]

            if directions[i] == "R":
                stack.append(i)
                continue

            while stack and healths[i]:
                if healths[stack[-1]] > healths[i]:
                    healths[i] = 0
                    healths[stack[-1]] -= 1
                elif healths[stack[-1]] < healths[i]:
                    healths[i] -= 1
                    healths[stack[-1]] = 0
                    stack.pop()
                else:
                    healths[i] = 0
                    healths[stack[-1]] = 0
                    stack.pop()

        return [healths[i] for i in range(N) if healths[i] != 0]
