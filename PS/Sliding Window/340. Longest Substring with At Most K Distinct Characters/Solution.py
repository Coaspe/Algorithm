import collections

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not k: return 0
        l, r = 0, 0
        dic = collections.defaultdict(int)
        answer = 0

        while r < len(s):
          dic[s[r]] = r
          if len(dic) > k:
            val, idx = min(dic.items(), key=lambda x: x[1])
            del dic[val]
            l = idx + 1

          answer = max(answer, r - l + 1)
          r += 1
          
        return answer