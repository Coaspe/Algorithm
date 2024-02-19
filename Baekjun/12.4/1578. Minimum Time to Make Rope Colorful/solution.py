class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        prev, acc, max_t = "", 0, 0
        colors = list(colors)
        ans = 0

        while colors:
            c, t = colors.pop(), neededTime.pop()

            if prev and prev[-1] == c:
                acc += t
                max_t = max(max_t, t)
                prev += c
            else:
                if len(prev) > 1:
                    ans += acc - max_t

                prev = c
                max_t = acc = t

        if len(prev) > 1:
            ans += acc - max_t

        return ans
