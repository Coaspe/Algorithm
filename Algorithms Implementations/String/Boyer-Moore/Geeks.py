NO_OF_CHARS = 256


def badCharHeuristic(string, size):
    badChar = [-1] * NO_OF_CHARS

    for i in range(size):
        badChar[ord(string[i])] = i

    return badChar


def search(txt, pat):
    m = len(pat)
    n = len(txt)

    badChar = badCharHeuristic(pat, m)

    s = 0
    while (s <= n-m):
        j = m-1

        while j >= 0 and pat[j] == txt[s+j]:
            j -= 1

        # 패턴과 일치
        if j == -1:
            print("Pattern occur at shift = {}".format(s))

            '''
				Shift the pattern so that the next character in text
					aligns with the last occurrence of it in pattern.
				The condition s+m < n is necessary for the case when
				pattern occurs at the end of text
			'''
            s += (m-badChar[ord(txt[s+m])] if s+m < n else 1)
        # 패턴과 불일치
        else:
            '''
            Shift the pattern so that the bad character in text
            aligns with the last occurrence of it in pattern. The
            max function is used to make sure that we get a positive
            shift. We may get a negative shift if the last occurrence
            of bad character in pattern is on the right side of the
            current character.
            '''
            s += max(1, j-badChar[ord(txt[s+j])])


def main():
    txt = "ABAAABCDABC"
    pat = "ABC"
    search(txt, pat)


if __name__ == '__main__':
    main()

# This code is contributed by Atul Kumar
# (www.facebook.com/atul.kr.007)
