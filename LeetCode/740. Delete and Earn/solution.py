from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        c = Counter(nums)

        key = set(c.keys())
        s = list(reversed(sorted(key)))

        max_a = [0, c[s[0]] * s[0]]

        for v in s[1:]:
            new_max_a = [0, 0]
            new_max_a[0] = max(max_a)
            new_max_a[1] = max(max_a) + c[v] * v

            if v + 1 in key:
                new_max_a[1] = max_a[0] + c[v] * v

            max_a = new_max_a[:]

        return max(max_a)
