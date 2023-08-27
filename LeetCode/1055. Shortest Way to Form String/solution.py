class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        t = 0
        ans = 0

        for _ in range(len(target)):
            tmp_t = t

            for i in range(len(source)):
                if source[i] == target[t]:
                    t += 1

                if t == len(target):
                    break

            if tmp_t != t:
                ans += 1

            if t == len(target):
                break

        return -1 if t != len(target) else ans
