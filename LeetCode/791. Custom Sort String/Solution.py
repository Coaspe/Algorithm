from collections import defaultdict


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dic = defaultdict(int)
        for idx, c in enumerate(order):
            dic[c] = idx
        return ''.join(sorted(list(s), key=lambda x: dic[x]))
