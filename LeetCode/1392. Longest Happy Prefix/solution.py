class Solution:
    def longestPrefix(self, s: str) -> str:
        table = [0 for _ in range(len(s))]
        i = 0

        for j in range(1, len(s)):

            while i > 0 and s[i] != s[j]:
                i = table[i - 1]

            if s[i] == s[j]:
                i += 1
                table[j] = i

        return s[: table[-1]]
