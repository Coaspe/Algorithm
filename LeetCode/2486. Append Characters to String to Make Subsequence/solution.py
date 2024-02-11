class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l = r = 0

        while r < len(t):
            if s[l] == t[r]:
                l += 1
                r += 1
            else:
                l += 1

            if l == len(s):
                return len(t) - r

        return 0
