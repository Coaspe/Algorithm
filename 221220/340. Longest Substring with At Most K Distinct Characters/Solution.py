from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not k:
            return 0
        l, r = 0, 0
        dic = defaultdict(int)
        answer = 0

        while r < len(s):
            dic[s[r]] += 1

            while len(dic) > k:
                dic[s[l]] -= 1
                if not dic[s[l]]:
                    del dic[s[l]]
                l += 1

            answer = max(answer, r - l + 1)
            r += 1

        return answer
