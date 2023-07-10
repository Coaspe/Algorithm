from typing import List
'''
    0 exit
    1 enter
'''


class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        n = len(arrival)
        exits = []
        enters = []
        status = 0
        ans = [-1] * n
        for i in range(n-1, -1, -1):
            if state[i]:
                enters.append(i)
            else:
                exits.append(i)

        for t, i in enumerate(arrival):
            arrive_s = state[i]
