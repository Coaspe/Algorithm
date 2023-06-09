from typing import List
import collections


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        counter = collections.Counter(nums)
        N, P, check = set(), set(), set()
        for i in counter.keys():
            if i > 0:
                P.add(i)
            elif i < 0:
                N.add(i)

        if counter[0] >= 3:
            answer.append([0, 0, 0])

        for p in P:
            for n in N:
                if p == -2*n and counter[n] >= 2:
                    answer.append([n, n, p])
                    continue
                if n == -2*p and counter[p] >= 2:
                    answer.append([n, p, p])
                    continue

                # Check -(p+n) exists and exclude duplicated elements.
                if counter[-(p+n)] and not n == -2*p and not p == -2*n and \
                        (-(p+n), n, p) not in check and (n, p, -(p+n)) not in check:
                    answer.append([n, -(p+n), p])
                    check.add((n, -(p+n), p))
        return answer
