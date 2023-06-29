from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_counter = Counter(s)
        t_counter = Counter(t)
        ans = 0
        for s_key in s_counter.keys():
            if s_key not in t_counter:
                ans += s_counter[s_key]
            elif s_counter[s_key] > t_counter[s_key]:
                ans += s_counter[s_key] - t_counter[s_key]

        return ans
