from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        words.reverse()
        line = []

        while words:
            word = words.pop()
            n = len(word)

            if n == maxWidth:
                ans.append(word)
                continue

            line = [word]

            while words and n < maxWidth:
                word = words.pop()
                L = len(line)

                if n + len(word) + L > maxWidth:
                    if L != 1:
                        q, m = divmod(maxWidth - n, (L - 1))
                        blanks = [q] * (L - 1)

                        for i in range(m):
                            blanks[i] += 1

                        blanks.append(0)
                    else:
                        blanks = [maxWidth - n]

                    tmp_ans = ""

                    for i in range(L):
                        tmp_ans += line[i]
                        tmp_ans += blanks[i] * " "

                    ans.append(tmp_ans)
                    line = []

                    words.append(word)
                    break

                line.append(word)
                n += len(word)

        if line:
            t = " ".join(line)
            t += " " * (maxWidth - len(t))
            ans.append(t)

        return ans
