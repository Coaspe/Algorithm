from collections import Counter
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        answer = []
        counter = Counter(nums)
        flag = len(counter.keys())

        while flag:
            tmp = []
            for key in counter.keys():
                if counter[key]:
                    counter[key] -= 1
                    if not counter[key]:
                        flag -= 1
                    tmp.append(key)
            answer.append(tmp)
        return answer
