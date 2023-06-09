from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: 'str') -> 'int':
        n = len(s)
        if n < 3:
            return n

        answer = 0
        left, right = 0, 0
        added = defaultdict(int)

        while right < n:
            added[s[right]] = right
            if len(added) >= 3:
                val, idx = min(added.items(), key=lambda x: x[1])
                del added[val]
                left = idx + 1

            answer = max(answer, right - left + 1)
            right += 1


        return answer
                

