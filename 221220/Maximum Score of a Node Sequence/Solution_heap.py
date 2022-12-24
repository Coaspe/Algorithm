from typing import List
from heapq import heappush, heappop
from collections import defaultdict


def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:

    def func(a, b):
        heappush(D[a], (scores[b], b))
        if len(D[a]) > 3:
            heappop(D[a])

    D = defaultdict(list)

    for i, j in edges:
        func(i, j)
        func(j, i)

    ans = -1

    for i, j in edges:

        if len(D[i]) < 2 or len(D[j]) < 2:
            continue

        for n1 in D[i]:
            for n2 in D[j]:
                if n1[1] not in [i, j] and n2[1] not in [i, j] and n1[1] != n2[1]:
                    ans = max(ans, scores[i] + scores[j] + n1[0] + n2[0])

    return ans
