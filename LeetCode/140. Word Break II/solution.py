from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dic = set(wordDict)

        memo = {}

        def dfs(s):
            if s in memo:
                return memo[s]

            ans = []

            if s in dic:
                ans = [s]

            for i in range(1, len(s) + 1):
                ss = s[:i]
                if ss in dic:
                    right = dfs(s[i:])
                    for r in right:
                        ans.append(ss + " " + r)
            memo[s] = ans

            return memo[s]

        return dfs(s)
