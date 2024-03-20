class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12 or len(s) < 4:
            return []

        def check(c):
            if not c or (c != "0" and c[0] == "0") or int(c) > 255 or len(c) > 3:
                return True
            return False

        ans = []
        for a, b, c in itertools.combinations(range(1, len(s)), 3):
            a, b, c, d = s[:a], s[a:b], s[b:c], s[c:]

            if check(a) or check(b) or check(c) or check(d):
                continue
            ans.append(f"{a}.{b}.{c}.{d}")

        return ans
